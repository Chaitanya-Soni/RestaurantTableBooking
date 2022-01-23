from django.contrib import admin
from .models import table,BookingTime
# Register your models here.
@admin.register(table)
class TableModel(admin.ModelAdmin):
    list_display=["id","name","seats"]
@admin.register(BookingTime)
class BookingModel(admin.ModelAdmin):
    list_display= ["id","tablebook","stime","etime"]