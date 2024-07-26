from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categorias/', include('categorias.urls')),
    path('productos/', include('productos.urls')),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
