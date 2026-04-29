from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'business_name']
    readonly_fields = ['created_at']