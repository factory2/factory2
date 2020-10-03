from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

def articles(request):
    articles = Article.objects.all().order_by('code')
    return render(request, 'articles/articles.html', {'articles': articles})

def article_detail(request, code):
    article = get_object_or_404(Article, code=code)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('article_detail', code=article.code)
    else:
        form = ArticleForm()
        return render(request, 'articles/article_edit.html', {'form': form}, locals())

def article_edit(request, code):
    article = get_object_or_404(Article, code=code)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('article_detail', code=article.code)
    else:
        form = ArticleForm(instance=article)
        return render(request, 'articles/article_edit.html', {'form': form}, locals())
