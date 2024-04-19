from django.contrib import admin

# Register your models here.

from site_app.models import Produto
admin.site.register(Produto)

from site_app.models import Usuario
admin.site.register(Usuario)
