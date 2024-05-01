
# from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    
    path('', views.home,name="home"),
    path('roupas', views.page_roupas, name='roupas'),
    path('roupa/<produto_id>', views.page_roupa_detalhe, name='roupa_detalhe'),
    path('login', views.page_login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registro', views.page_registro, name='registro'),
    path('registro-influencer', views.page_registro_influencer, name='registro_influencer'),
    path('remove-acount', views.removeAccount, name='remove_account'),
    path('sobre', views.page_about, name='sobre'),
    
    # admin routes
    
    path('auth/create-product', views.page_registroProduto, name='createProduct'),
     
]
