from django.contrib import admin
from .models import Dashboard
# Register your models here.

@admin.register(Dashboard)

class AdminDashboard(admin.ModelAdmin):
    list_display=["id","Title","Description"]

