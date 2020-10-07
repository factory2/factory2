from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Zamak
from .forms import ZamakForm

def zamak(request):
    zamak = Zamak.objects.all().order_by('slug')
    return render(request, 'zamak/zamak.html', {'zamak': zamak})

def zamak_detail(request, slug):
    zamak = get_object_or_404(Zamak, slug=slug)
    return render(request, 'zamak/zamak_detail.html', {'zamak': zamak})

def zamak_new(request):
    if request.method == "POST":
        form = ZamakForm(request.POST, request.FILES)
        if form.is_valid():
            zamak = form.save(commit=False)
            zamak.save()
            return redirect('zamak_detail', slug=zamak.slug)
    else:
        form = ZamakForm()
        return render(request, 'zamak/zamak_edit.html', {'form': form}, locals())

def zamak_edit(request, slug):
    zamak = get_object_or_404(Zamak, slug=slug)
    if request.method == "POST":
        form = ZamakForm(request.POST, request.FILES, instance=zamak)
        if form.is_valid():
            zamak = form.save(commit=False)
            zamak.save()
            return redirect('zamak_detail', slug=zamak.slug)
    else:
        form = ZamakForm(instance=zamak)
        return render(request, 'zamak/zamak_edit.html', {'form': form}, locals())
