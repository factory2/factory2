from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ThermalDeburrer, BasketDeburring, ParameterDeburring
from .forms import ThermalDeburrerForm, BasketDeburringForm, ParameterDeburringForm


# Thermal deburrer machine

def thermal_deburrers(request):
    thermal_deburrers = ThermalDeburrer.objects.all().order_by('name')
    baskets_deburring = BasketDeburring.objects.all().order_by('title')
    parameters_deburring = ParameterDeburring.objects.all().order_by('title')
    return render(request, 'machines/thermal_deburrers.html', { 'thermal_deburrers': thermal_deburrers, 'baskets_deburring': baskets_deburring, 'parameters_deburring': parameters_deburring })

def thermal_deburrer_detail(request, pk):
    thermal_deburrer = get_object_or_404(ThermalDeburrer, pk=pk)
    return render(request, 'machines/thermal_deburrer_detail.html', { 'thermal_deburrer': thermal_deburrer })

def thermal_deburrer_new(request):
    if request.method == "POST":
        form = ThermalDeburrerForm(request.POST, request.FILES)
        if form.is_valid():
            thermal_deburrer = form.save(commit=False)
            thermal_deburrer.save()
            return redirect('thermal_deburrer_detail', pk=thermal_deburrer.pk)
        else:
            return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())
    else:
        form = ThermalDeburrerForm()
        return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())

def thermal_deburrer_edit(request, pk):
    thermal_deburrer = get_object_or_404(ThermalDeburrer, pk=pk)
    if request.method == "POST":
        form = ThermalDeburrerForm(request.POST, request.FILES, instance=thermal_deburrer)
        if form.is_valid():
            thermal_deburrer = form.save(commit=False)
            thermal_deburrer.save()
            return redirect('thermal_deburrer_detail', pk=thermal_deburrer.pk)
    else:
        form = ThermalDeburrerForm(instance=thermal_deburrer)
        return render(request, 'machines/thermal_deburrer_edit.html', {'form': form}, locals())


def basket_deburring_detail(request, pk):
    basket_deburring = get_object_or_404(BasketDeburring, pk=pk)
    return render(request, 'machines/basket_deburring_detail.html', { 'basket_deburring': basket_deburring })

def basket_deburring_new(request):
    if request.method == "POST":
        form = BasketDeburringForm(request.POST, request.FILES)
        if form.is_valid():
            basket_deburring = form.save(commit=False)
            basket_deburring.save()
            return redirect('basket_deburring_detail', pk=basket_deburring.pk)
        else:
            return render(request, 'machines/basket_deburring_edit.html', {'form': form}, locals())
    else:
        form = BasketDeburringForm()
        return render(request, 'machines/basket_deburring_edit.html', {'form': form}, locals())

def basket_deburring_edit(request, pk):
    basket_deburring = get_object_or_404(ThermalDeburrer, pk=pk)
    if request.method == "POST":
        form = BasketDeburringForm(request.POST, request.FILES, instance=basket_deburring)
        if form.is_valid():
            basket_deburring = form.save(commit=False)
            basket_deburring.save()
            return redirect('basket_deburring_detail', pk=basket_deburring.pk)
    else:
        form = BasketDeburringForm(instance=basket_deburring)
        return render(request, 'machines/basket_deburring_edit.html', {'form': form}, locals())


def parameter_deburring_detail(request, pk):
    parameter_deburring = get_object_or_404(ParameterDeburring, pk=pk)
    return render(request, 'machines/parameter_deburring_detail.html', { 'parameter_deburring': parameter_deburring })

def parameter_deburring_new(request):
    if request.method == "POST":
        form = ParameterDeburringForm(request.POST)
        if form.is_valid():
            parameter_deburring = form.save(commit=False)
            parameter_deburring.save()
            return redirect('parameter_deburring_detail', pk=parameter_deburring.pk)
        else:
            return render(request, 'machines/parameter_deburring_edit.html', {'form': form},)
    else:
        form = ParameterDeburringForm()
        return render(request, 'machines/parameter_deburring_edit.html', {'form': form},)

def parameter_deburring_edit(request, pk):
    parameter_deburring = get_object_or_404(ThermalDeburrer, pk=pk)
    if request.method == "POST":
        form = ParameterDeburringForm(request.POST, request.FILES, instance=parameter_deburring)
        if form.is_valid():
            parameter_deburring = form.save(commit=False)
            parameter_deburring.save()
            return redirect('parameter_deburring_detail', pk=parameter_deburring.pk)
    else:
        form = ParameterDeburringForm(instance=parameter_deburring)
        return render(request, 'machines/parameter_deburring_edit.html', {'form': form}, locals())
