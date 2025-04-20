from django.shortcuts import render
from .models import Turn
from .forms import TurnForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from datetime import datetime
import calendar
from django.db.models import Count
from django.db.models.functions import TruncDate

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

class TurnAvailableView(ListView):
    model = Turn
    template_name = "available_turns.html"
    context_object_name = "available_turns"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get current year and month
        today = datetime.now()
        year = self.request.GET.get('year', today.year)
        month = self.request.GET.get('month', today.month)
        year, month = int(year), int(month)
        
        # Create calendar data
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]
        
        # Get all turns for this month
        first_day = datetime(year, month, 1)
        if month == 12:
            last_day = datetime(year + 1, 1, 1)
        else:
            last_day = datetime(year, month + 1, 1)
            
        turns = Turn.objects.filter(
            date__gte=first_day,
            date__lt=last_day
        ).annotate(
            day=TruncDate('date')
        ).values('date').annotate(
            count=Count('id')
        )
        
        # Create turns_by_date list of tuples for easier template access
        turns_by_date = {}
        for turn in turns:
            turns_by_date[turn['date'].day] = turn['count']
        
        # Previous and next month links
        if month == 1:
            prev_month = 12
            prev_year = year - 1
        else:
            prev_month = month - 1
            prev_year = year
            
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        context.update({
            'calendar': cal,
            'month_name': month_name,
            'year': year,
            'turns_by_date': turns_by_date,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
            'current_month': month,
        })
        return context

