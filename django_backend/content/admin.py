from django.contrib import admin
from django.utils.html import format_html
from .models import MultimediaItem, Cliente, Newsletter, Servicio, Contacto

@admin.register(MultimediaItem)
class MultimediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'image_preview', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', 'created_at']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "Sin imagen"
    image_preview.short_description = "Vista previa"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active', 'logo_preview', 'website', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    ordering = ['order', 'name']
    
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.logo.url)
        return "Sin logo"
    logo_preview.short_description = "Logo"

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at', 'unsubscribed_at']
    list_filter = ['is_active', 'subscribed_at', 'unsubscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at', 'unsubscribed_at']
    ordering = ['-subscribed_at']
    
    actions = ['unsubscribe_selected']
    
    def unsubscribe_selected(self, request, queryset):
        for newsletter in queryset:
            newsletter.unsubscribe()
        self.message_user(request, f"{queryset.count()} suscriptores han sido desuscritos.")
    unsubscribe_selected.short_description = "Desuscribir seleccionados"

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'image_preview', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', 'title']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "Sin imagen"
    image_preview.short_description = "Vista previa"

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['direccion', 'telefono', 'email', 'updated_at']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Solo permitir una instancia
        return not Contacto.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar la información de contacto
        return False
