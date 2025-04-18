from django.shortcuts import render
from apps.barber.models import Barber
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BarberListView(ListView):
    model = Barber
    template_name = "index_barber.html"
    context_object_name= "barbers"

class BarberDetailView(DetailView):
    model = Barber
    template_name = 'detail_barber.html'

class BarberCreateView(CreateView):
    model= Barber
    template_name = "formulario_barber.html"
    fields = ['name', 'email', 'phone']
    success_url = reverse_lazy('barber:index_barber') # redirigo al index de barbers una vez creado 


class BarberUpdateView(UpdateView):
    model = Barber
    template_name = 'formulario_barber.html'
    fields = ['name', 'email', 'phone'] # Campos que se mostrarán en el formulario
    success_url = reverse_lazy('barber:index_barber') # Redirigir después de editar el producto

class BarberDeleteView(DeleteView):
    model = Barber
    template_name = 'delete_barber.html'
    success_url = reverse_lazy('barber:index_barber') # Redirigir después de eliminar el producto