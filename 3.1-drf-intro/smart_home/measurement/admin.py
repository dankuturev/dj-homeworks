from django.contrib import admin

from .models import Measurements, Sensor


class MeasurementInline(admin.TabularInline):
    model = Measurements
    extra = 0


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]
    pass


@admin.register(Measurements)
class MeasurementAdmin(admin.ModelAdmin):
    pass

# Register your models here.
