from django.db import models
from django.utils import timezone

class MultimediaItem(models.Model):
    """Modelo para los elementos multimedia (imágenes del carrusel)"""
    title = models.CharField(max_length=200, verbose_name="Título")
    image = models.ImageField(upload_to='multimedia/', verbose_name="Imagen")
    description = models.TextField(blank=True, verbose_name="Descripción")
    order = models.IntegerField(default=0, verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Elemento Multimedia"
        verbose_name_plural = "Elementos Multimedia"

    def __str__(self):
        return self.title

class Cliente(models.Model):
    """Modelo para los clientes"""
    name = models.CharField(max_length=200, verbose_name="Nombre")
    logo = models.ImageField(upload_to='clientes/', verbose_name="Logo")
    website = models.URLField(blank=True, verbose_name="Sitio web")
    order = models.IntegerField(default=0, verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    """Modelo para suscriptores del newsletter"""
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de suscripción")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    unsubscribed_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de desuscripción")

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    def __str__(self):
        return self.email

    def unsubscribe(self):
        """Marca el suscriptor como inactivo"""
        self.is_active = False
        self.unsubscribed_at = timezone.now()
        self.save()

class Servicio(models.Model):
    """Modelo para los servicios"""
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='servicios/', verbose_name="Imagen")
    order = models.IntegerField(default=0, verbose_name="Orden")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.title

class Contacto(models.Model):
    """Modelo para información de contacto"""
    direccion = models.CharField(max_length=500, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    horario_lunes_viernes = models.CharField(max_length=100, verbose_name="Horario Lunes-Viernes")
    horario_sabado = models.CharField(max_length=100, verbose_name="Horario Sábado")
    horario_domingo = models.CharField(max_length=100, verbose_name="Horario Domingo")
    whatsapp = models.CharField(max_length=20, blank=True, verbose_name="WhatsApp")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Información de Contacto"
        verbose_name_plural = "Información de Contacto"

    def __str__(self):
        return "Información de Contacto"

    def save(self, *args, **kwargs):
        # Asegurar que solo haya una instancia
        if not self.pk and Contacto.objects.exists():
            return
        super().save(*args, **kwargs)
