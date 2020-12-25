from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ThermalDeburring, PalletThermalDeburred
from .forms import ThermalDeburringForm

def articles_thermal_deburring(request):
    articles_thermal_deburring = ThermalDeburring.objects.all()
    return render(request, 'tasks/articles_thermal_deburring.html', {'articles_thermal_deburring': articles_thermal_deburring})

def article_thermal_deburring_detail(request, article_code):
    article_thermal_deburring = get_object_or_404(ThermalDeburring, article__code=article_code)
    return render(request, 'tasks/article_thermal_deburring_detail.html', {'article_thermal_deburring': article_thermal_deburring})

def article_thermal_deburring_new(request):
    if request.method == "POST":
        form = ThermalDeburringForm(request.POST)
        if form.is_valid():
            article_thermal_deburring = form.save(commit=False)
            article_thermal_deburring.save()
            return redirect('article_thermal_deburring_detail', article_code=article_thermal_deburring)
    else:
        form = ThermalDeburringForm()
        return render(request, 'tasks/article_thermal_deburring_edit.html', {'form': form})

def article_thermal_deburring_edit(request, article_code):
    article_thermal_deburring = get_object_or_404(ThermalDeburring, article__code=article_code)
    if request.method == "POST":
        form = ThermalDeburringForm(request.POST, instance=article_thermal_deburring)
        if form.is_valid():
            article_thermal_deburring = form.save(commit=False)
            article_thermal_deburring.save()
            return redirect('article_thermal_deburring_detail', article_code=article_thermal_deburring)
    else:
        form = ThermalDeburringForm(instance=article_thermal_deburring)
        return render(request, 'tasks/article_thermal_deburring_edit.html', {'form': form})

