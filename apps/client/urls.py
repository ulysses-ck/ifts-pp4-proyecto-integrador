from django.urls import path, include
from . import views
app_name = 'client' #defino el namespace para las urls
urlpatterns = [
    path('',views.ClientHome.as_view(), name='home_client'),
    path('reservar/<int:time_slot_id>/', views.ClientCreateWithTurnView.as_view(), name='create_with_turn'),
    path('confirmacion/<int:turno_id>/', views.SuccessView.as_view(), name='success'),

    path('list/', views.ClientListView.as_view(), name='list_client'),
    path('update/<int:pk>/', views.ClientUpdateView.as_view(), name='update_client'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='delete_client'),
]