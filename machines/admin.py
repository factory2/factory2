from django.contrib import admin
from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ThermalDeburrerResource(resources.ModelResource):

    class Meta:
        model = ThermalDeburrer

class ThermalDeburrerAdmin(ImportExportModelAdmin):
    resource_class = ThermalDeburrerResource

class BasketDeburringResource(resources.ModelResource):

    class Meta:
        model = BasketDeburring

class BasketDeburringAdmin(ImportExportModelAdmin):
    resource_class = BasketDeburringResource

class ParameterDeburringResource(resources.ModelResource):

    class Meta:
        model = ParameterDeburring

class ParameterDeburringAdmin(ImportExportModelAdmin):
    resource_class = ParameterDeburringResource

admin.site.register(ParameterDeburring, ParameterDeburringAdmin)
admin.site.register(BasketDeburring, BasketDeburringAdmin)
admin.site.register(ThermalDeburrer, ThermalDeburrerAdmin)
