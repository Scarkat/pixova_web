from rest_framework import serializers
from .models import MultimediaItem, Cliente, Newsletter, Servicio, Contacto

class MultimediaItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = MultimediaItem
        fields = ['id', 'title', 'image', 'image_url', 'description', 'order', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class ClienteSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Cliente
        fields = ['id', 'name', 'logo', 'logo_url', 'website', 'order', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def get_logo_url(self, obj):
        if obj.logo:
            return self.context['request'].build_absolute_uri(obj.logo.url)
        return None

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'email', 'subscribed_at', 'is_active']
        read_only_fields = ['id', 'subscribed_at']

class ServicioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Servicio
        fields = ['id', 'title', 'description', 'image', 'image_url', 'order', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id', 'direccion', 'telefono', 'email', 'horario_lunes_viernes', 
                 'horario_sabado', 'horario_domingo', 'whatsapp', 'updated_at']
        read_only_fields = ['id', 'updated_at']

# Serializers para listas (solo campos públicos)
class MultimediaItemListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = MultimediaItem
        fields = ['id', 'title', 'image_url', 'description', 'order']
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

class ClienteListSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Cliente
        fields = ['id', 'name', 'logo_url', 'website', 'order']
    
    def get_logo_url(self, obj):
        if obj.logo:
            return self.context['request'].build_absolute_uri(obj.logo.url)
        return None

class ServicioListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Servicio
        fields = ['id', 'title', 'description', 'image_url', 'order']
    
    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None 