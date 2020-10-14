from django.urls import path

from . import views

urlpatterns = [
    path('', views.zamak, name='zamak'),
    path('<slug:slug>', views.zama_detail, name='zama_detail'),
    path('<slug:slug>/edit/', views.zama_edit, name='zama_edit'),
    path('new/', views.zama_new, name='zama_new'),
]
