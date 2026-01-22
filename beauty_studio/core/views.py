from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Client, Master, Service, Appointment, Order, Review, Promotion
from .serializers import (
    ClientSerializer, MasterSerializer, ServiceSerializer,
    AppointmentSerializer, OrderSerializer, ReviewSerializer, PromotionSerializer
)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

@api_view(['GET'])
def appointments_today(request):
    today = timezone.now().date()
    appointments = Appointment.objects.filter(datetime__date=today)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)