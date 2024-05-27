
# from django.contrib import admin
from django.urls import path
from api_prova_app import views

urlpatterns = [
    path('produtos', views.produtos),
    path('produto/<produto_id>', views.produto_id),
    
    path('relacoes', views.relacoes),
    path('relacao/<relacao_id>', views.relacao_id),
    
      
]
 