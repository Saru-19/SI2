from django.contrib import admin
from .models import Tarjeta, Pago

@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    pass