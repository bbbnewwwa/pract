from django.db import models

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    duration_minutes = models.PositiveIntegerField('Длительность (мин)', default=30)
    image = models.ImageField('Изображение', upload_to='services/', blank=True, null=True)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f"{self.name} — {self.price} ₽"