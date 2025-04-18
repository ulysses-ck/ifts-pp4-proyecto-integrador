from django.urls import path, include
from . import views
app_name = 'barber' #defino el namespace para las urls
urlpatterns = [
    path('',views.BarberListView.as_view(), name='index_barber'),
    path('create/',views.BarberCreateView.as_view(), name='create_barber'),
    path('<int:pk>/update/',views.BarberUpdateView.as_view(), name='update_barber'),
    path('<int:pk>/delete/',views.BarberDeleteView.as_view(), name='delete_barber'),
    path('<int:pk>/detail/',views.BarberDetailView.as_view(), name='detail_barber'),
]
