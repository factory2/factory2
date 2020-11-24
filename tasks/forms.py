from django import forms

from .models import ThermalDeburring

class ThermalDeburringForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburring
        fields = ('code', 'basket_deburring', 'parameter_deburring', 'description')
