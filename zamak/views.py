from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Zamak
from .forms import ZamaForm

def zamak(request):
    zamak = Zamak.objects.all().order_by('slug')
    return render(request, 'zamak/zamak.html', {'zamak': zamak})

def zama_detail(request, slug):
    zama = get_object_or_404(Zamak, slug=slug)
    return render(request, 'zamak/zama_detail.html', {'zama': zama})

def zama_new(request):
    if request.method == "POST":
        form = ZamaForm(request.POST, request.FILES)
        if form.is_valid():
            zama = form.save(commit=False)
            zama.save()
            return redirect('zama_detail', slug=zama.slug)
    else:
        form = ZamaForm()
        return render(request, 'zamak/zama_edit.html', {'form': form}, locals())

def zama_edit(request, slug):
    zama = get_object_or_404(Zamak, slug=slug)
    if request.method == "POST":
        form = ZamaForm(request.POST, request.FILES, instance=zama)
        if form.is_valid():
            zama = form.save(commit=False)
            zama.save()
            return redirect('zama_detail', slug=zama.slug)
    else:
        form = ZamaForm(instance=zama)
        return render(request, 'zamak/zama_edit.html', {'form': form}, locals())
