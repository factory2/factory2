from django import forms

from .models import ThermalDeburring, PalletThermalDeburred

class ThermalDeburringForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburring
        fields = ('article', 'basket_deburring', 'parameter_deburring', 'description')


class PalletThermalDeburredForm(forms.ModelForm):

    class Meta:
        model = PalletThermalDeburred
        fields = ('pallet', 'thermal_deburred_date', 'quantity_no_ok',)
