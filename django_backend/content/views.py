from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import MultimediaItem, Cliente, Newsletter, Servicio, Contacto
from .serializers import (
    MultimediaItemSerializer, MultimediaItemListSerializer,
    ClienteSerializer, ClienteListSerializer,
    NewsletterSerializer, ServicioSerializer, ServicioListSerializer,
    ContactoSerializer
)

# Create your views here.

class MultimediaItemViewSet(viewsets.ModelViewSet):
    queryset = MultimediaItem.objects.filter(is_active=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return MultimediaItemListSerializer
        return MultimediaItemSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return MultimediaItem.objects.all()
        return MultimediaItem.objects.filter(is_active=True)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(is_active=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ClienteListSerializer
        return ClienteSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cliente.objects.all()
        return Cliente.objects.filter(is_active=True)

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'El email es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar si ya existe
        if Newsletter.objects.filter(email=email).exists():
            return Response(
                {'error': 'Este email ya está registrado'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'], permission_classes=[])
    def subscribe(self, request):
        """Endpoint público para suscribirse al newsletter"""
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'El email es requerido'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verificar si ya existe
        newsletter, created = Newsletter.objects.get_or_create(
            email=email,
            defaults={'is_active': True}
        )
        
        if not created and newsletter.is_active:
            return Response(
                {'error': 'Este email ya está suscrito'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        elif not created and not newsletter.is_active:
            newsletter.is_active = True
            newsletter.unsubscribed_at = None
            newsletter.save()
        
        serializer = self.get_serializer(newsletter)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.filter(is_active=True)
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ServicioListSerializer
        return ServicioSerializer
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Servicio.objects.all()
        return Servicio.objects.filter(is_active=True)

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        # Solo permitir una instancia
        if Contacto.objects.exists():
            return Response(
                {'error': 'Ya existe información de contacto'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'], permission_classes=[])
    def info(self, request):
        """Endpoint público para obtener información de contacto"""
        contacto = Contacto.objects.first()
        if not contacto:
            return Response(
                {'error': 'No hay información de contacto disponible'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = self.get_serializer(contacto)
        return Response(serializer.data)
