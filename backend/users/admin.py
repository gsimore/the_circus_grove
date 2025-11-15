from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin for custom User model."""
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'coach', 'is_staff', 'created_at']
    list_filter = ['user_type', 'is_staff', 'is_superuser', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'bio', 'date_of_birth', 'height_cm')}),
        ('User Type & Coach', {'fields': ('user_type', 'coach')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'phone', 'bio', 'date_of_birth', 'height_cm'),
        }),
        ('Coach Assignment', {
            'fields': ('coach',),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']

