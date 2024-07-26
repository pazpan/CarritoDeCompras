from django.contrib import messages
from urllib import request
from django.shortcuts import redirect, render
from categorias.models import Categoria


def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render (request,'listar_categoria.html',
                   context={'categorias':categorias,})
    
    
    
def Guardar_categoria(request):
    nombre = request.POST['nombre']
    
    categoria = Categoria.objects.create(
        nombre=nombre)
    return redirect ('/categorias')



def Editar_categoria(request,id_categoria):
    try:
        if request.method =="POST":
            nombre=request.POST['nombre']
        
               
            categoria=Categoria.objects.get(id_categoria=id_categoria)
            categoria.nombre=nombre

            categoria.save() 
            
            
            messages.success(request,"!Categoria actualizada correctamente¡")
            return redirect("/categorias")
        
    except Exception as e: 
            messages.error(request, f"No se pudo actualizar la categoria: {e}")
  
   
    categorias = Categoria.objects.get(id_categoria=id_categoria)
    return render(request,'editar_categoria.html',context={'categorias':categorias})

    

    




def Eliminar_categoria(request, id_categoria):
    try:
       
        categoria = Categoria.objects.get(id_categoria=id_categoria)
        categoria.delete()  
      
        messages.success(request, '¡Categoría eliminada correctamente!')
        return redirect('/categorias')  
    except Exception as e:
       
        messages.error(request, f"No se pudo eliminar la categoría: {e}")
        return redirect('/categorias')  

