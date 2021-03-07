from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, Pallet
from .forms import ArticleNewForm, ArticleEditForm, PalletForm
from tasks.models import PalletThermalDeburred
from rest_framework import viewsets
from .serializers import ArticleSerializer

def articles(request):
    articles = Article.objects.all().order_by('code')
    return render(request, 'articles/articles.html', {'articles': articles})

def article_detail(request, code):
    article = get_object_or_404(Article, code=code)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_new(request):
    if request.method == "POST":
        form = ArticleNewForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('article_detail', code=article.code)
        else:
            return render(request, 'articles/article_new.html', {'form': form}, locals())
    else:
        form = ArticleNewForm()
        return render(request, 'articles/article_new.html', {'form': form}, locals())

def article_edit(request, code):
    article = get_object_or_404(Article, code=code)
    if request.method == "POST":
        form = ArticleEditForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            pallets = Pallet.objects.all()
            pallets_thermal_deburred = PalletThermalDeburred.objects.all()
            for pallet in pallets:
                if article.code == pallet.article.code:
                    pallet.weight = article.weight * pallet.quantity / 1000
                    pallet.save()
            for pallet_thermal_deburred in pallets_thermal_deburred:
                if article.code == pallet_thermal_deburred.pallet.article.code:
                    pallet_thermal_deburred.weight = pallet_thermal_deburred.quantity * article.weight / 1000
                    pallet_thermal_deburred.save()
            article.save()
            return redirect('article_detail', code=article.code)
    else:
        form = ArticleEditForm(instance=article)
        return render(request, 'articles/article_edit.html', {'form': form}, locals())


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


def pallets(request):
    pallets = Pallet.objects.all()
    pallets_thermal_deburred = PalletThermalDeburred.objects.all()
    for pallet in pallets:
        for pallet_thermal_deburred in pallets_thermal_deburred:
            if pallet.article == pallet_thermal_deburred.pallet.article:
                pallet.thermal_deburred = True
                pallet.save()
    return render(request, 'production/pallets.html', {'pallets': pallets})


def pallet_new(request):
    if request.method == "POST":
        form = PalletForm(request.POST)
        if form.is_valid():
            pallet = form.save(commit=False)
            pallet.weight = pallet.article.weight * pallet.quantity / 1000 # Weight pallet in kg
            pallet.save()
            return redirect('pallets')
    else:
        form = PalletForm()
        return render(request, 'production/pallet_new.html', {'form': form})


def pallets_thermal_deburred(request):
    pallets_thermal_deburred = PalletThermalDeburred.objects.all()
    return render(request, 'articles/pallets_thermal_deburred.html', {'pallets_thermal_deburred': pallets_thermal_deburred})
