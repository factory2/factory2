from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, ThermalDeburring

def articles(request):
    articles = Article.objects.all().order_by('code')
    return render(request, 'articles/articles.html', {'articles': articles})

def article_detail(request, code):
    article = get_object_or_404(Article, code=code)
    return render(request, 'articles/article_detail.html', {'article': article})

def thermal_deburring_articles(request):
    thermal_deburring_articles = ThermalDeburring.objects.all()
    return render(request, 'articles/thermal_deburring_articles.html', {'thermal_deburring_articles':thermal_deburring_articles})

def thermal_deburring_article_detail(request, slug):
    thermal_deburring_article = get_object_or_404(ThermalDeburring, slug=slug)
    return render(request, 'articles/thermal_deburring_article_detail.html', {'thermal_deburring_article':thermal_deburring_article})
