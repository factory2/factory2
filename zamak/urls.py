from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.zamak, name='zamak'),
    path('all/<slug:slug>/', views.zama_detail, name='zama_detail'),
    path('all/<slug:slug>/edit/', views.zama_edit, name='zama_edit'),
    path('new/', views.zama_new, name='zama_new'),
]
