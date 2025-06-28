from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MultimediaItemViewSet, ClienteViewSet, NewsletterViewSet,
    ServicioViewSet, ContactoViewSet
)

router = DefaultRouter()
router.register(r'multimedia', MultimediaItemViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'newsletter', NewsletterViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'contacto', ContactoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] 