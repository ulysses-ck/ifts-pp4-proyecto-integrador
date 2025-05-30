from datetime import date
from django.shortcuts import redirect, render
from apps.barber.models import Barber
from apps.client.form import ClientForm
from apps.client.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

from apps.turn.models import TimeSlot, Turn

# Create your views here.

class ClientHome(ListView):
    template_name = 'home_cliente.html'
    context_object_name = 'available_slots'

    def get_queryset(self):
        # No retornamos queryset aquí, lo manejamos en get_context_data
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        
        all_slots = TimeSlot.objects.filter(is_active=True)
        barbers = Barber.objects.all()
        
        available_slots = []

        for slot in all_slots:
            reserved_barbers = Turn.objects.filter(date=today, time_slot=slot).values_list('barber_id', flat=True) #obtengo los barbers reservados
            if barbers.exclude(id__in=reserved_barbers):
                available_slots.append(slot)
        context.update({
            'available_slots': available_slots,
            'avaible_barbers': barbers,
            'today': today,
        })

        return context

class ClientCreateWithTurnView(CreateView):
    """Vista para crear cliente y asignar turno simultáneamente"""
    model = Client
    form_class = ClientForm
    template_name = 'formulario_client.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        time_slot_id = self.kwargs.get('time_slot_id')
        if time_slot_id:
            try:
                time_slot = TimeSlot.objects.get(id=time_slot_id)
                today = date.today()
                busy_barber_ids = Turn.objects.filter(
                    date=today,
                    time_slot=time_slot
                ).values_list('barber_id', flat=True)

                context['selected_time_slot'] = time_slot
                context['available_barbers'] = Barber.objects.exclude(id__in=busy_barber_ids)
            except TimeSlot.DoesNotExist:
                context['available_barbers'] = Barber.objects.all()
        else:
            context['available_barbers'] = Barber.objects.all()
        
        return context
    
    def form_valid(self, form):
        # Guardar el cliente
        client = form.save()
        
        # Obtener datos del formulario POST
        time_slot_id = self.kwargs.get('time_slot_id')
        barber_id = self.request.POST.get('barber')
        
        if time_slot_id and barber_id:
            try:
                time_slot = TimeSlot.objects.get(id=time_slot_id)
                barber = Barber.objects.get(id=barber_id)
                
                # Verificar que el turno aún esté disponible
                today = date.today()
                existing_turn = Turn.objects.filter(
                    date=today,
                    time_slot=time_slot,
                    barber=barber
                ).exists()
                
                if not existing_turn:
                    # Crear el turno
                    Turn.objects.create(
                        client=client,
                        barber=barber,
                        date=today,
                        time_slot=time_slot
                    )
                    
                    # # Enviar email de confirmación
                    # self.send_confirmation_email(client, barber, time_slot, today)
                    
                    return redirect('client:success')
                else:
                    # El turno ya fue reservado por otro cliente
                    form.add_error(None, "Lo sentimos, este horario ya fue reservado por otro cliente.")
                    return self.form_invalid(form)
                    
            except (TimeSlot.DoesNotExist, Barber.DoesNotExist):
                form.add_error(None, "Error en la selección de horario o barbero.")
                return self.form_invalid(form)
        
        return super().form_valid(form)

def client_success_view(request):
    """Vista de confirmación después de reservar turno"""
    return render(request, 'success.html')


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