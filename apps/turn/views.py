from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from apps import turn
from apps.Usuarios.forms import LoginForm, RegisterForm
from apps.client import form
from apps.turn.api.chistes import get_random_joke
from apps.turn.forms import TurnForm
from .models import Turn
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from datetime import datetime, timedelta
import calendar
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from apps.core.views import MyLoginRequiredMixin

SPANISH_MONTHS = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
    5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
    9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

def some_logic_to_decide_confirmation():
    raise NotImplementedError

# Create your views here.


class TurnHome(MyLoginRequiredMixin, ListView):
    model = Turn
    template_name = "home_turn.html"
    context_object_name = "turns"

    
    def get_queryset(self):
        queryset = super().get_queryset()
        date_param = self.request.GET.get('date')
        
        if date_param:
            try:
                filter_date = datetime.strptime(date_param, '%Y-%m-%d').date()
                queryset = queryset.filter(date=filter_date)
            except ValueError:
                pass  # Si la fecha no es válida, retornamos todos los turnos
                
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_param = self.request.GET.get('date')
        
        if date_param:
            try:
                filter_date = datetime.strptime(date_param, '%Y-%m-%d').date()
                context['selected_date'] = filter_date
            except ValueError:
                pass
    
      # Agregamos el chiste al contexto, solo es de test esto
        context['joke'] = get_random_joke()
        return context
                
    

class TurnCreate(MyLoginRequiredMixin, CreateView):
    form_class = TurnForm
    template_name = "formulario_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class ConfirmTurnView(View):
    template_name = 'confirm_turn.html'

    def get(self, request, pk):
        turn = get_object_or_404(Turn, pk=pk)
        if turn.is_confirmed:
            return redirect('turn:home_turn')
        return render(request, self.template_name, {'turn': turn})

    def post(self, request, pk):
        turn = get_object_or_404(Turn, pk=pk)
        confirm = request.POST.get('confirm')

        if confirm == 'yes':
            turn.is_confirmed = True
        elif confirm == 'no':
            turn.is_confirmed = None

        turn.save()
        self.send_confirmation_email(turn)
        return redirect('turn:home_turn')
     
    
    def send_confirmation_email(self, turn):
        from django.conf import settings
        from django.core.mail import send_mail

        joke = get_random_joke()  # obtenemos el chiste dinámicamente

        subject = 'Confirmación de Turno'
        message = (
            f'Tienes un turno confirmado con {turn.barber.name} el {turn.date} a las {turn.time_slot}.\n\n'
            f'Y para que te rías un poco:\n{joke}'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [turn.client.email]

        response = send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=True,
        )
        return response


    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     # Get the turn instance that was just created
    #     turn = self.object

   

class TurnUpdate(MyLoginRequiredMixin, UpdateView):
    model = Turn
    form_class = TurnForm
    template_name = "formulario_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class TurnDelete(MyLoginRequiredMixin, DeleteView):
    model = Turn
    template_name = "delete_turn.html"
    success_url = reverse_lazy('turn:home_turn')

class TurnDetail(MyLoginRequiredMixin, DetailView):
    model = Turn
    template_name = "detail_turn.html"
    context_object_name= "turn"


class TurnAvailableWeekView(MyLoginRequiredMixin, ListView):
    model = Turn
    template_name = "available_turns_week.html"
    context_object_name = "available_turns"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        
        try:
            year = int(self.request.GET.get('year', today.year))
            month = int(self.request.GET.get('month', today.month))
            day = int(self.request.GET.get('day', today.day))
            current_date = datetime(year, month, day).date()
        except (ValueError, TypeError):
            current_date = today

        # Calculate start of week (Monday)
        days_since_monday = current_date.weekday()
        week_start = current_date - timedelta(days=days_since_monday)
        
        # Generate week dates (Monday to Sunday)
        week_dates = [week_start + timedelta(days=i) for i in range(7)]
        
        # Get turns for the week
        week_end = week_start + timedelta(days=6)
        turns = Turn.objects.filter(
            date__gte=week_start, 
            date__lte=week_end
        ).select_related('client', 'time_slot').order_by('date', 'time_slot__start_time')

        # Group turns by date
        turns_by_date = {}
        clients_by_date = {}
        
        for turn in turns:
            day = turn.date.day
            if day not in turns_by_date:
                turns_by_date[day] = 0
                clients_by_date[day] = []
            
            turns_by_date[day] += 1
            clients_by_date[day].append({
                'id': turn.id,
                'name': turn.client.name,
                'time': turn.time_slot.start_time.strftime('%H:%M'),
                'barber': turn.barber.name if hasattr(turn, 'barber') else 'N/A'
            })

        # Calculate navigation dates
        prev_week = week_start - timedelta(days=7)
        next_week = week_start + timedelta(days=7)

        context.update({
            'view_type': 'week',
            'current_date': current_date,
            'week_dates': week_dates,
            'turns_by_date': turns_by_date,
            'clients_by_date': clients_by_date,
            
            # Previous week navigation
            'prev_week_year': prev_week.year,
            'prev_week_month': prev_week.month,
            'prev_week_day': prev_week.day,
            
            # Next week navigation  
            'next_week_year': next_week.year,
            'next_week_month': next_week.month,
            'next_week_day': next_week.day,
        })
        
        return context


class TurnAvailableMonthView(MyLoginRequiredMixin, ListView):
    model = Turn
    template_name = "available_turns_month.html"
    context_object_name = "available_turns"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now()
        try:
            year = int(self.request.GET.get('year', today.year))
            month = int(self.request.GET.get('month', today.month))
        except (ValueError, TypeError):
            year, month = today.year, today.month

        cal = calendar.monthcalendar(year, month)
        month_name = SPANISH_MONTHS[month]

        first_day = datetime(year, month, 1)
        if month == 12:
            last_day = datetime(year + 1, 1, 1)
        else:
            last_day = datetime(year, month + 1, 1)

        turns = Turn.objects.filter(date__gte=first_day, date__lt=last_day).annotate(
            day=TruncDate('date')
        ).values('date').annotate(count=Count('id'))

        turns_by_date = {turn['date'].day: turn['count'] for turn in turns}

        if month == 1:
            prev_month, prev_year = 12, year - 1
        else:
            prev_month, prev_year = month - 1, year

        if month == 12:
            next_month, next_year = 1, year + 1
        else:
            next_month, next_year = month + 1, year

        context.update({
            'view_type': 'month',
            'calendar': cal,
            'month_name': month_name,
            'year': year,
            'turns_by_date': turns_by_date,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
            'current_month': month,
            'current_day': today.day if month == today.month and year == today.year else None,
        })
        return context