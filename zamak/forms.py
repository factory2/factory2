from django import forms

from .models import Zamak

class ZamaForm(forms.ModelForm):

    class Meta:
        model = Zamak
        fields = ('title', 'description', 'image1', 'image2', 'image3', 'image4',)
