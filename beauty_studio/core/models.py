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

class Service(models.Model):
    CATEGORIES = Master.SPECIALIZATIONS
    name = models.CharField('Название', max_length=100)
    category = models.CharField('Категория', max_length=20, choices=CATEGORIES)
    duration_minutes = models.PositiveIntegerField('Длительность (мин)')
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} — {self.price} ₽"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Запланировано'),
        ('completed', 'Выполнено'),
        ('cancelled', 'Отменено'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    datetime = models.DateTimeField('Дата и время')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='scheduled')
    total_amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.client} → {self.master} ({self.datetime})"

class Order(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('online', 'Онлайн'),
    ]
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, verbose_name='Запись')
    total_amount = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2)
    payment_method = models.CharField('Способ оплаты', max_length=20, choices=PAYMENT_METHODS)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)

    def __str__(self):
        return f"Чек #{self.id} — {self.total_amount} ₽"

class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField('Оценка', choices=[(i, i) for i in range(1, 6)])
    text = models.TextField('Текст отзыва', blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.client} — {self.rating}"
