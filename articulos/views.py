from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Articulo
from .forms import ArticuloForm
# Create your views here.

# Cremaos las vistas basdas en clases con el modelo qyue tiene que usar

class StaffRequiredMixin(object):
    """
    Requiere que el usuario sea staff
    """

    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)


class ArticuloListView(ListView):
    model = Articulo

class ArticuloDetailView(DetailView):
    model = Articulo

@method_decorator(staff_member_required,name='dispatch')
class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    success_url = reverse_lazy('articulo:articulos') 
    # puede haber un customize widgets= {} (googlear)

@method_decorator(staff_member_required,name='dispatch')
class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name_suffix = "_update_form" 
    success_url = reverse_lazy('articulo:articulos')

    def get_success_url(self): 
        """" 
        Vuelve a formulario de edicion
        """
        return reverse_lazy('articulo:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required,name='dispatch')
class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulo:articulos')

    
    



