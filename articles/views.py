from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})

def article_detail(request, code):
    article = get_object_or_404(Article, code=code)
    return render(request, 'articles/article_detail.html', {'article': article})
