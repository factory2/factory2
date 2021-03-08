from django import forms
from articles.models import Pallet
from .models import ThermalDeburring

class ThermalDeburringNewForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburring
        fields = ('article', 'basket_deburring', 'parameter_deburring', 'description')

class ThermalDeburringEditForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburring
        fields = ('basket_deburring', 'parameter_deburring', 'description')

class PalletThermalDeburredNewForm(forms.ModelForm):
    class Meta:
        model = Pallet
        fields = ('quantity_thermal_deburred', 'thermal_deburred_date', 'quantity_thermal_deburred_no_ok')
