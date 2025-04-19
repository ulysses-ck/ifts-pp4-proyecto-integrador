from django.shortcuts import render
from .models import Turn
from .forms import TurnForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

# Create your views here.

class TurnHome(ListView):
    model = Turn
    template_name = "home_turn.html"
    context_object_name= "turns"
    
class TurnCreate(CreateView):
    model = Turn
    form_class = TurnForm
    template_name = "formulario_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class TurnUpdate(UpdateView):
    model = Turn
    form_class = TurnForm
    template_name = "formulario_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class TurnDelete(DeleteView):
    model = Turn
    template_name = "delete_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class TurnDetail(DetailView):
    model = Turn
    template_name = "detail_turn.html"
    context_object_name= "turn"

