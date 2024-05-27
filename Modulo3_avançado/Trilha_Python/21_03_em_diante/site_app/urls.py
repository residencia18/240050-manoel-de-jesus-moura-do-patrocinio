
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
    path('user/edit', views.page_editperfil, name='edicao'),
    path('search',views.search, name='search'),
    
    # admin routes
    
    path('auth/registro-categoria', views.page_registerCategory, name='add_categoria'),
    path('auth/create-product', views.page_registroProduto, name='createProduct'),
    path('auth/create-user', views.page_admCadUser, name='addUser'),
    path('auth/edit-user/<user_id>', views.page_admEditUser, name='admEditUser'),
    path('auth/painel', views.page_painelAdmin, name='painel'),
    path('auth/toggleactive/<user_id>', views.toggleactive, name="toggleactive"),    
    path('auth/create-group', views.page_group, name="addGroup"),    
]
 