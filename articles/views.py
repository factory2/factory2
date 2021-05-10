from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, Pallet
from .forms import ArticleNewForm, ArticleEditForm, PalletForm, PalletThermalDeburredNewForm
from tasks.models import ThermalDeburring, PalletThermalDeburred
from django.utils import timezone

current_year = timezone.now().strftime("%Y")
current_month = timezone.now().strftime("%m")

def articles(request):
    articles = Article.objects.all().order_by('code')
    return render(request, 'articles/articles.html', {'articles': articles, 'current_year': current_year, 'current_month': current_month })

def article_detail(request, code):
    article = get_object_or_404(Article, code=code)
    pallets = Pallet.objects.all().filter(article__code=code)
    if pallets:
        list_article_quantity_produced = []
        for pallet in pallets:
            list_article_quantity_produced.append(pallet.quantity)
        article_quantity_produced = sum(list_article_quantity_produced)
        return render(request, 'articles/article_detail.html', {'article': article, 'article_quantity_produced': article_quantity_produced})
    else:
        return render(request, 'articles/article_detail.html', {'article': article})

def article_new(request):
    if request.method == "POST":
        form = ArticleNewForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            if article.for_thermal_deburring:
                article.save()
                article_thermal_deburring = ThermalDeburring(article=article)
                article_thermal_deburring.save()
                return redirect('article_thermal_deburring_edit', article_code = article.code)
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
            for pallet in pallets:
                if article.code == pallet.article.code:
                    pallet.weight = article.weight * pallet.quantity / 1000
                    if pallet.thermal_deburred == True:
                        pallet.weight_thermal_deburred_no_ok = pallet.quantity_thermal_deburred_no_ok * article.weight / 1000
                        pallet.weight_thermal_deburred = pallet.quantity_thermal_deburred * article.weight / 1000
                    pallet.save()
            article.save()
            if hasattr(article, 'thermaldeburring') == True and article.for_thermal_deburring:
                return redirect('article_thermal_deburring_edit', article_code = article.code)
            elif article.for_thermal_deburring:
                article_thermal_deburring = ThermalDeburring(article=article)
                article_thermal_deburring.save()
                return redirect('article_thermal_deburring_edit', article_code = article.code)
            elif hasattr(article, 'thermaldeburring'):
                article_thermal_deburring = ThermalDeburring.objects.get(article=article)
                article_thermal_deburring.delete()
                return redirect('article_detail', code=article.code)
            else:
                return redirect('article_detail', code=article.code)
    else:
        form = ArticleEditForm(instance=article)
        return render(request, 'articles/article_edit.html', {'form': form}, locals())

def pallets(request):
    pallets = Pallet.objects.all()
    pallets_count = len(pallets)
    heading = "All pallets"
    return render(request, 'articles/pallets.html', { 'pallets': pallets, 'current_year': current_year, 'current_month': current_month, 'pallets_count': pallets_count, 'heading': heading })

def pallets_current_month(request, year, month):
    pallets = Pallet.objects.filter(created_date__year = year, created_date__month = month)
    pallets_count = len(pallets)
    heading = "Pallets"
    date = str(year) + "/" + str(month)
    return render(request, 'articles/pallets.html', { 'pallets': pallets, 'date': date, 'current_year': year, 'current_month': month, 'heading': heading, 'pallets_count': pallets_count })

def pallets_for_thermal_deburring(request):
    heading = "Pallets for thermal deburring"
    pallets = Pallet.objects.filter(article__for_thermal_deburring = True, thermal_deburred = False)
    return render(request, 'articles/pallets.html', { 'pallets': pallets, 'current_year': current_year, 'current_month': current_month, 'heading': heading })

def pallets_thermal_deburred(request):
    pallets = Pallet.objects.filter(thermal_deburred = True).order_by('-thermal_deburred_date')
    pallets_count = len(pallets)
    heading = "Pallets thermal deburred"
    return render(request, 'articles/pallets.html', { 'pallets': pallets, 'current_year': current_year, 'current_month': current_month, 'heading': heading , 'pallets_count': pallets_count })

def pallets_thermal_deburred_current_month(request, year, month):
    pallets = Pallet.objects.filter(thermal_deburred = True, thermal_deburred_date__year = year, thermal_deburred_date__month = month).order_by('-thermal_deburred_date')
    pallets_count = len(pallets)
    date = str(year) + "/" + str(month)
    heading = "Pallets thermal deburred"
    return render(request, 'articles/pallets.html', { 'pallets': pallets, 'current_year': current_year, 'current_month': current_month, 'heading': heading, 'date': date, 'pallets_count': pallets_count })

def pallet_new(request):
    if request.method == "POST":
        form = PalletForm(request.POST)
        if form.is_valid():
            pallet = form.save(commit=False)
            pallet.employee = request.user
            pallet.weight = pallet.article.weight * pallet.quantity / 1000 # Weight pallet in kg
            pallet.save()
            return redirect('pallets_current_month', year=current_year, month=current_month)
    else:
        form = PalletForm()
        return render(request, 'articles/pallet_new.html', {'form': form})

def pallet_thermal_deburred_new(request, pk):
    pallet = get_object_or_404(Pallet, pk=pk)
    if request.method == "POST":
        form = PalletThermalDeburredNewForm(request.POST, instance=pallet)
        if form.is_valid():
            pallet = form.save(commit=False)
            if pallet.quantity >= pallet.quantity_thermal_deburred_no_ok:
                pallet.employee_thermal_deburring = request.user
                pallet.quantity_thermal_deburred = pallet.quantity - pallet.quantity_thermal_deburred_no_ok
                pallet.weight_thermal_deburred_no_ok = pallet.quantity_thermal_deburred_no_ok * pallet.article.weight / 1000
                pallet.weight_thermal_deburred = pallet.quantity_thermal_deburred * pallet.article.weight / 1000
                pallet.thermal_deburred = True
                pallet.save()
                return redirect('pallets_thermal_deburred_current_month', year=current_year, month=current_month)
            else:
                error = "The quantity article no ok can't be more than quantity of all articles in the pallet"
                return render(request, 'articles/pallet_thermal_deburred_new.html', { 'form': form, 'error':error })
        else:
            return render(request, 'articles/pallet_thermal_deburred_new.html', {'form': form})
    else:
        form = PalletThermalDeburredNewForm()
        return render(request, 'articles/pallet_thermal_deburred_new.html', {'form': form})
