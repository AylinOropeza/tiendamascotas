from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'producto'

urlpatterns = [
    path('', login_required(views.ProductoListView.as_view()), name='index'),
    path('detalle-producto/<int:pk>/', login_required(views.ProductoDetailView.as_view()), name='detalle_producto'),
    path('crear-producto/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('actualizar-producto/<int:pk>/', views.ProductoUpdateView.as_view(), name='actualizar_producto'),
    path('eliminar-producto/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto')
]
