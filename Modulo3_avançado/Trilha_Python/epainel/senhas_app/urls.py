from django.urls import path
from senhas_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('encerrar/', views.encerrar, name="encerrar"),
    path('editarperfil/', views.editarperfil, name="editarperfil"),    

    path('caduser/', views.caduser, name="caduser"),
    path('painel/', views.painel, name="painel"),    
    path('toggleactive/<id>', views.toggleactive, name="toggleactive"),    
]