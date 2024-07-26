from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from categorias.models import Categoria
from productos.models import Productos



#Función que lista productos
def Listar_producto(request):
    try:
        # Obtener todos los productos y todas las categorías
        producto = Productos.objects.all()
        categoria=Categoria.objects.all()
         # Renderizar la plantilla 'producto.html' con los productos y categorías obtenidos
        return render (request,'listar_producto.html', context={'productos':producto,'categoria':categoria})
    #Muestra mensaje de error
    except Exception as e:
            messages.error(request, e)


def Guardar_producto(request):
    try:
        # Obtener los datos del formulario
        nombre=request.POST['nombre']
        precio=int(request.POST['precio'])
        stock=request.POST['stock']
        descripcion=request.POST['descripcion']
        id_categoria=request.POST['categoria']
        
        # Obtener la categoría relacionada al producto
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        # Crear el objeto Producto y guardarlo en la base de datos
        producto = Productos.objects.create(nombre=nombre,precio=precio,
                                           stock=stock,descripcion=descripcion,
                                        categoria=categoria
                                        )
        # Mostrar mensaje de éxito
        messages.success(request,"!Producto ingresado correctamente¡")
        # Redireccionar a la página de productos
        return redirect('/productos')
    except Exception as e:
        # Muestra mensaje de error 
        messages.error(request, f"No se pudo ingresar el producto: {e}")
     # Redireccionar a la página de productos en caso de error
    return redirect('/productos')


#Función para actualizar un producto
def Editar_producto(request, id_producto):
    # Manejar la solicitud POST para actualizar el producto
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        descripcion=request.POST['descripcion']
        categoria = request.POST['categoria']
        
        try:
            # Obtener el producto a editar por su id_producto
            producto = Productos.objects.get(id_producto=id_producto)
            
            # Actualizar los campos del producto con los nuevos datos del formulario
            producto.nombre = nombre
            producto.precio = precio
            producto.stock = stock
            producto.descripcion=descripcion
            producto.categoria = Categoria.objects.get(id_categoria=categoria)
            
            # Guardar los cambios en la base de datos
            producto.save()
            
            # Mostrar mensaje de éxito si la actualización fue exitosa
            messages.success(request, "¡Producto actualizado correctamente!")
            
            # Redirigir a la lista de productos después de la actualización
            return redirect("/productos")
        
        except Exception as e:
            # Capturar y manejar cualquier excepción que ocurra durante la actualización
            messages.error(request, f"No se puede actualizar el producto: {e}")
            
        # Redirigir a la lista de productos en caso de error
        return redirect("/productos")

    # Manejar la solicitud GET para mostrar el formulario de edición
    producto = Productos.objects.get(id_producto=id_producto)
    categorias = Categoria.objects.all()
    
    # Renderizar a la pagina 'editar_producto.html' con los datos del producto y las categorías
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias})




#Función para eliminar un producto
def Eliminar_producto(request,id_producto):
    try:
        #Obtiene el producto por su id_producto y lo elimina
        producto = Productos.objects.get(id_producto=id_producto)
        # Eliminar el producto de la base de datos
        producto.delete()
         # Mostrar mensaje de éxito
        messages.success(request,"!Producto eliminado correctamente¡")
        
        #Redirige a la pagina producto
        return redirect("/productos")
    #Muestra mensaje de error
    except Exception as e:
            messages.error(request, "No se puedo eliminar el producto")