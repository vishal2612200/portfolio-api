from django.contrib import admin
from .models import Trade

# Register your models here.
@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    pass

