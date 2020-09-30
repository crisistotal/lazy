from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Tipo(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Articulo(models.Model):
    nombre = models.CharField(verbose_name='Nombre',max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True, blank=True,default=1)
    precio = models.IntegerField(verbose_name='Precio')
    cantidad = models.IntegerField(verbose_name='Cantidad',max_length=20)
    descripcion = RichTextField(verbose_name='Descripcion',max_length=50,null=True,blank=True)
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Edicion")

    class meta:
        verbose_name = 'Articulo'
        verbose_name_plural  = 'Articulos'
        ordening = ['order','cantidad','precio']

    def __str__(self):
        return self.nombre
    
    @property
    def get_capital(self):
        capital = self.precio * self.cantidad
        return capital

        






