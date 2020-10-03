from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('code', 'title', 'description', 'image1', 'image2', 'image3', 'image4',)
