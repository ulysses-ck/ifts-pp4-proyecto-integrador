from django.shortcuts import render
from apps.client.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

# Create your views here.

class ClientHome(View):
    def get(self, request):
        return render(request, 'home_cliente.html')
    
class CLientCreateView(CreateView):
    model = Client
    template_name = "formulario_client.html"
    fields = ['name', 'email', 'phone']
    success_url = reverse_lazy('client:list_client')

class ClientListView(ListView):
    model = Client
    template_name = 'list-client.html'
    context_object_name = 'clients'
    ordering = ['name']

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'formulario_client.html'
    fields = ['name', 'email', 'phone']
    success_url = reverse_lazy('client:list_client')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client:list_client')