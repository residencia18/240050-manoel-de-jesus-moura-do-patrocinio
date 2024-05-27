

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('site_app.urls')),
    path('api/', include('api_app.urls')),
    path('api2/', include('api_prova_app.urls'))
    
]
