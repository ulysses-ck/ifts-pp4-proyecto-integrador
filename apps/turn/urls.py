from django.urls import path, include
from . import views

app_name = 'turn'

urlpatterns = [
    path('', views.TurnHome.as_view(), name='home_turn'),
    path('create/', views.TurnCreate.as_view(), name='create_turn'),
    path('<int:pk>/update/', views.TurnUpdate.as_view(), name='update_turn'),
    path('<int:pk>/delete/', views.TurnDelete.as_view(), name='delete_turn'),
    path('<int:pk>/detail/', views.TurnDetail.as_view(), name='detail_turn'),
    path('available/week/', views.TurnAvailableWeekView.as_view(), name='available_week'),
    path('available/month/', views.TurnAvailableMonthView.as_view(), name='available_month'),
    path('confirm/<int:pk>/', views.ConfirmTurnView.as_view(), name='confirm_turn'),
]
