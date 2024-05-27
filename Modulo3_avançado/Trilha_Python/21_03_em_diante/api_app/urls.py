
# from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('roupas', views.roupas),
    path('roupas/<produto_id>', views.roupas_id),
      
]
 