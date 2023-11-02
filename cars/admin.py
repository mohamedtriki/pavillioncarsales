from django.contrib import admin
from .models import vehicle,feature,model


# Register your models here.
admin.site.register(feature)
admin.site.register(model)
@admin.register(vehicle)
class vehicleadmin(admin.ModelAdmin):
    list_display=('title','date')