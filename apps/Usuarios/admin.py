from django.contrib import admin
from apps.Usuarios.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username', 'role')
    list_filter = ('role',)
