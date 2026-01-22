from django.contrib import admin
from .models import Client, Master, Service, Appointment, Order, Review, Promotion

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone')

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'commission_percent')
