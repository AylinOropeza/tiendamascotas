from django.contrib import admin
from .models import Marca, Categoria, Producto

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion',)
    list_display = ('nombre_producto', 'stock', 'marca', 'categoria', 'fecha_vencimiento', 'public')
    search_fields = (
        'nombre_producto',
        'categoria__categoria_producto'
    )
    list_filter = (
        'marca',
        'fecha_vencimiento'
    )
    ordering = (
        'nombre_producto',
        'stock'
    )
    fieldsets = [
        (None,
            {'fields': [
                'nombre_producto',
                'imagen_producto',
                'stock', 'precio',
                'marca',
                'categoria',
                'fecha_vencimiento'
            ]
        }),
        ('Additional information', {'fields': ['fecha_creacion', 'public']})
    ]
    
admin.site.register(Marca)
admin.site.register(Categoria)