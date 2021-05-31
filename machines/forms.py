from django import forms

from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring

class ThermalDeburrerForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburrer
        fields = ("__all__")

class BasketDeburringForm(forms.ModelForm):

    class Meta:
        model = BasketDeburring
        fields = ('title', 'description', 'image',)

class ParameterDeburringForm(forms.ModelForm):

    class Meta:
        model = ParameterDeburring
        fields = ('title', 'description',)
