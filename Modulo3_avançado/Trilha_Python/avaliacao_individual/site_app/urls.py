
# from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    path('produtos', views.produtos),
    path('produto/<produto_id>', views.produto_id),

      
]
 