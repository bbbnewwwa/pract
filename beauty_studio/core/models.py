from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=150)
    phone = models.CharField('Телефон', max_length=20, unique=True)

    def __str__(self):
        return self.full_name

class Master(models.Model):
    SPECIALIZATIONS = [
        ('nails', 'Ногти'),
        ('lashes', 'Ресницы'),
        ('brows', 'Брови'),
        ('hair', 'Парикмахер'),
        ('cosmetology', 'Косметология'),
    ]

full_name = models.CharField('ФИО', max_length=150)
phone = models.CharField('Телефон', max_length=20)
specialization = models.CharField('Специализация', max_length=20, choices=SPECIALIZATIONS)
work_schedule = models.TextField('График работы', blank=True)
commission_percent = models.DecimalField('Процент от услуг', max_digits=5, decimal_places=2, default=0)

def __str__(self):
        return f"{self.full_name} ({self.get_specialization_display()})"

