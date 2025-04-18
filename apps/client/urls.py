from django.urls import path, include
from . import views
app_name = 'client' #defino el namespace para las urls
urlpatterns = [
    path('',views.ClientHome.as_view(), name='Home_client'),
    path('create/',views.CLientCreateView.as_view(), name='create_client'),
]
