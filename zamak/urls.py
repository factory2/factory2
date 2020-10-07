from django.urls import path

from . import views

urlpatterns = [
    path('', views.zamak, name='zamak'),
    path('all/<slug>', views.zamak_detail, name='zamak_detail'),
    path('new/', views.zamak_new, name='zamak_new'),
    path('<slug>/edit/', views.zamak_edit, name='zamak_edit'),
]
