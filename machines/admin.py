from django.contrib import admin

from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring

admin.site.register(ThermalDeburrer)
admin.site.register(BasketDeburring)
admin.site.register(ParameterDeburring)
