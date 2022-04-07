from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Marca(models.Model):
    nombre_marca = models.CharField('Marca', max_length=200, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        
    def __str__(self):
        return self.nombre_marca
    
class Categoria(models.Model):
    categoria_producto = models.CharField('Categoría', max_length=100, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
    def __str__(self):
        return self.categoria_producto
    
class Producto(models.Model):
    nombre_producto = models.CharField('Nombre del Producto', unique=True, max_length=200, null=False, blank=False)
    imagen_producto = models.ImageField('Imagen del producto', upload_to='productos/', null=False, blank=False)
    stock = models.IntegerField('Cantidad', default=0)
    precio = models.FloatField('Precio', default=00.0)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateTimeField('Fecha de vencimiento', null=False, blank=False)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)
    public = models.BooleanField('Público', default=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    @admin.display(
        boolean=True,
        description='Expiración del producto:'
    )
    
    def producto_expirado(self):
        producto_expirado = self.fecha_vencimiento < timezone.now()
        if (producto_expirado and self.public) or self.stock == 0:
            self.public = False
            self.save()
        elif not producto_expirado and not self.public and self.stock > 0:
            self.public = True
            self.save()
        return producto_expirado
    
    def __str__(self):
        return self.nombre_producto
        