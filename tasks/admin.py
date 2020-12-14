from django.contrib import admin
from .models import ThermalDeburring, PalletThermalDeburred
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ThermalDeburringResource(resources.ModelResource):

    class Meta:
        model = ThermalDeburring
        fields = ('article__code', 'basket_deburring__title', 'parameter_deburring__title')

class ThermalDeburringAdmin(ImportExportModelAdmin):
    resource_class = ThermalDeburringResource

admin.site.register(ThermalDeburring, ThermalDeburringAdmin)
admin.site.register(PalletThermalDeburred)
