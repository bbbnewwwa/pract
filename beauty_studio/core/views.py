from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Client, Master, Service, Appointment, Order, Review, Promotion
from .serializers import (
    ClientSerializer, MasterSerializer, ServiceSerializer,
    AppointmentSerializer, OrderSerializer, ReviewSerializer, PromotionSerializer
)
