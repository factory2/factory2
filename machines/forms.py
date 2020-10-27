from django import forms

from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring

class ThermalDeburrerForm(forms.ModelForm):

    class Meta:
        model = ThermalDeburrer
        fields = ('basket_deburring', 'parameter_deburring',)

class BasketDeburringForm(forms.ModelForm):

    class Meta:
        models = BasketDeburring
        fields = ('title', 'description', 'image',)

class ParameterDeburringForm(forms.ModelForm):

    class Meta:
        models = ParameterDeburring
        fields = ('title', 'description',)
