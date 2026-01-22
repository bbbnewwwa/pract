from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'masters', views.MasterViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'promotions', views.PromotionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('appointments/today/', views.appointments_today, name='appointments-today'),
]