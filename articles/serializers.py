
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'code', 'title', 'description', 'image1', 'image2', 'image3', 'image4',]

