from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=150)
    phone = models.CharField('Телефон', max_length=20, unique=True)

    def __str__(self):
        return self.full_name