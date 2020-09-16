from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ThermalDeburring

def articles_thermal_deburring(request):
    articles_thermal_deburring = ThermalDeburring.objects.all().order_by('slug')
    return render(request, 'tasks/articles_thermal_deburring.html', {'articles_thermal_deburring': articles_thermal_deburring})

def article_thermal_deburring_detail(request, slug):
    article_thermal_deburring = get_object_or_404(ThermalDeburring, slug=slug)
    return render(request, 'tasks/article_thermal_deburring_detail.html', {'article_thermal_deburring': article_thermal_deburring})
