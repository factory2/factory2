from django.contrib import admin
from .models import ThermalDeburring
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ThermalDeburringResource(resources.ModelResource):

    class Meta:
        model = ThermalDeburring

class ThermalDeburringAdmin(ImportExportModelAdmin):
    resource_class = ThermalDeburringResource

admin.site.register(ThermalDeburring, ThermalDeburringAdmin)
