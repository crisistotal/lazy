from django.contrib import admin
from .models import Articulo, Tipo

# Register your models here.
class ArticulosAdmin(admin.ModelAdmin):
    list_display= ('nombre','precio','cantidad','updated','order')

    class Media:
        css ={
            'all' : ('articulos/css/custom_ckeditor.css')
        }
class TipoAdmin(admin.ModelAdmin):
    list= ('tipo')

admin.site.register(Articulo ,ArticulosAdmin)
admin.site.register(Tipo, TipoAdmin)