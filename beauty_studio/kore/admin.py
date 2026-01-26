from django.contrib import admin
from .models import Client, Master, Service, Appointment, Order, Review, Promotion

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone')

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'commission_percent')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'duration_minutes')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'master', 'service', 'datetime', 'status', 'total_amount')
    list_filter = ('status', 'datetime')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'total_amount', 'payment_method', 'date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client', 'master', 'rating', 'date')

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percent', 'start_date', 'end_date')