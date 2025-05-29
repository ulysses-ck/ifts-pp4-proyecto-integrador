from django.urls import path, include
from . import views
app_name = 'client' #defino el namespace para las urls
urlpatterns = [
    path('',views.ClientListView.as_view(), name='list_client'),
    path('create/',views.CLientCreateView.as_view(), name='create_client'),
    path('update/<int:pk>/', views.ClientUpdateView.as_view(), name='update_client'),
    path('delete/<int:pk>/', views.ClientDeleteView.as_view(), name='delete_client'),
]
