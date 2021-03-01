from django import forms

from .models import Article, Pallet

class ArticleNewForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('code', 'title', 'for_thermal_deburring', 'description', 'weight', 'image1', 'image2', 'image3', 'image4',)

class ArticleEditForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'for_thermal_deburring', 'description', 'weight', 'image1', 'image2', 'image3', 'image4',)

class PalletForm(forms.ModelForm):
    class Meta:
        model = Pallet
        fields = ('article', 'quantity', 'created_date', 'department',)
