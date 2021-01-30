from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ThermalDeburring, PalletThermalDeburred
from .forms import ThermalDeburringForm, PalletThermalDeburredForm

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
            return render(request, 'tasks/article_thermal_deburring_edit.html', {'form': form})
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

def pallet_thermal_deburred_new(request):
    if request.method == "POST":
        form = PalletThermalDeburredForm(request.POST)
        if form.is_valid():
            pallet_thermal_deburred = form.save(commit=False)
            pallet_thermal_deburred.employee = request.user
            pallet_thermal_deburred.quantity = pallet_thermal_deburred.pallet.quantity - pallet_thermal_deburred.quantity_no_ok
            pallet_thermal_deburred.weight = pallet_thermal_deburred.quantity * pallet_thermal_deburred.pallet.article.weight / 1000
            pallet_thermal_deburred.save()
            return redirect('pallets_thermal_deburred')
        else:
            return render(request, 'tasks/pallet_thermal_deburred_edit.html', {'form': form})
    else:
        form = PalletThermalDeburredForm()
        return render(request, 'tasks/pallet_thermal_deburred_edit.html', {'form': form})
