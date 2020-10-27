from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring
from .forms import ThermalDeburrerForm, BasketDeburringForm, ParameterDeburringForm

def thermal_deburrers(request):
    thermal_deburrers = ThermalDeburrer.objects.all().order_by('title')
    return render(request, 'machines/thermal_deburrers.html', {'thermal_deburrers': thermal_deburrers})

def thermal_deburrer_detail(request, slug):
    thermal_deburrer = get_object_or_404(ThermalDeburrer, slug=slug)
    return render(request, 'machines/thermal_deburrer_detail.html', {'thermal_deburrer': thermal_deburrer})

def thermal_deburrer_new(request):
    if request.method == "POST":
        form = ThermalDeburrerForm(request.POST, request.FILES)
        if form.is_valid():
            thermal_deburrer = form.save(commit=False)
            thermal_deburrer.save()
            return redirect('thermal_deburrer_detail', slug=thermal_deburrer.slug)
        else:
            return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())
    else:
        form = ThermalDeburrerForm()
        return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())

def thermal_deburrer_edit(request, slug):
    thermal_deburrer = get_object_or_404(ThermalDeburrer, slug=slug)
    if request.method == "POST":
        form = ThermalDeburrerForm(request.POST, request.FILES, instance=thermal_deburrer)
        if form.is_valid():
            thermal_deburrer = form.save(commit=False)
            thermal_deburrer.save()
            return redirect('thermal_deburrer_detail', slug=thermal_deburrer.slug)
    else:
        form = ThermalDeburrerForm(instance=thermal_deburrer)
        return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())
