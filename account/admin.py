from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'created_at']
    list_display_links = ['id', 'username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name']


admin.site.register(User, UserAdmin)
