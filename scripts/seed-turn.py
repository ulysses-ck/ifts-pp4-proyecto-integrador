
from apps.turn.models import TimeSlot
from datetime import time, datetime, timedelta

def run():
    """Genera TimeSlots de 45 minutos desde 09:00 hasta 20:00"""
    
    # Limpiar TimeSlots existentes (opcional)
    TimeSlot.objects.all().delete()
    
    # Configuración
    start_hour = 9  # 09:00
    end_hour = 20   # 20:00
    duration_minutes = 45
    
    current_time = datetime.combine(datetime.today(), time(start_hour, 0))
    end_time = datetime.combine(datetime.today(), time(end_hour, 0))
    
    timeslots = []
    
    while current_time < end_time:
        # Calcular hora de fin del turno
        slot_end = current_time + timedelta(minutes=duration_minutes)
        
        # Verificar que no se pase de las 20:00
        if slot_end.time() <= time(end_hour, 0):
            timeslot = TimeSlot(
                start_time=current_time.time(),
                end_time=slot_end.time(),
                is_active=True
            )
            timeslots.append(timeslot)
        
        # Avanzar al siguiente slot (45 minutos después)
        current_time += timedelta(minutes=duration_minutes)
    
    # Crear todos los TimeSlots en la base de datos
    TimeSlot.objects.bulk_create(timeslots)
    
    print(f"✅ Se crearon {len(timeslots)} TimeSlots:")
    for slot in timeslots:
        print(f"   {slot.start_time.strftime('%H:%M')} - {slot.end_time.strftime('%H:%M')}")

if __name__ == '__main__':
    run()