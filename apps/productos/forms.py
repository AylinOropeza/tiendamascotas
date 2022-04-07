from datetime import timedelta

from django import forms
from django.utils import timezone, dateformat

from .models import Producto

formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        inputClass = 'mb-2 bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
        fields = ['nombre_producto', 'imagen_producto', 'stock', 'precio', 'marca', 'categoria', 'fecha_vencimiento']
        labels = {
            'nombre_producto': 'Nombre del producto',
            'imagen_producto': 'Imagen del producto',
            'stock': 'Cantidad disponible',
            'marca': 'Marca',
            'categoria': 'Categoría',
            'fecha_vencimiento': 'Fecha de vencimiento'
        }
        
        widgets = {
            'nombre_producto': forms.TextInput(
                attrs= {
                    'class': inputClass,
                    'placeholder': 'Nombre del producto'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': inputClass 
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': inputClass 
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class': inputClass 
                }
            ),
            'categoria': forms.Select(
                attrs={
                        'class': inputClass 
                    }
            ),
            'fecha_vencimiento': forms.DateTimeInput(
                format = '%Y-%m-%d %H:%M',
                attrs = {
                    #'type': 'date',
                    'class': inputClass,
                    'value': formatted_date,
                }
            )
        }
        
        def clean_stock(self):
            stock = self.cleaned_data.get('stock')
            if stock < 1 or stock > 100:
                raise forms.ValidationError('Ingrese un número entre 0 y 100', code='invalid')
            return stock
        
        def clean_price(self):
            precio = self.cleaned_data.get('precio')
            if precio < 1:
                raise forms.ValidationError('El precio debe ser mayor a 0', code='invalid')
            return precio
        
        def clean_fecha_vencimiento(self):
            fecha_vencimiento = self.cleaned_data['fecha_vencimiento']
            if fecha_vencimiento < (timezone.now() + timedelta(10)):
                self.add_error('fecha_vencimiento', 'La fecha de vencimiento debe ser a partir de 10 días desde hoy')
            return fecha_vencimiento