from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from .forms import ProductoForm
#from apps.sale.forms import AddCarForm

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'list.html', {'productos': productos})

class ProductoView(View):
    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        return render(request, "list.html", {'productos':productos})
    def post(self, request, *args, **kwargs):
        print("Dentro del método post()")
        return self.get(request)
    
class ProductoTemplateView(TemplateView, ProductoView):
    template_name = 'base.html'
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ProductoListView(ListView):
    template_name = 'productos/producto_list.html'
    context_object_name = 'productos'
    paginate_by = 4
    def get_queryset(self):
        productos = Producto.objects.filter(
            public=True,
            stock__gt = 0
        ).order_by('-precio')
        return productos
    
class ProductoDetailView(DetailView):
    model = Producto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['form'] = AddCarForm
        return context

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:index')
    
class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:index')
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView): 
    model = Producto
    success_url = reverse_lazy('producto:index')
    def post(self, pk):
        producto = self.model.objects.get(id=pk)
        producto.public = False
        producto.save()
        return redirect(self.success_url)
