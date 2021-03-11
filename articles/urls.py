from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.articles, name='articles'),
    path('new/', views.article_new, name='article_new'),
    path('edit', views.article_edit, name='article_edit'),
    path('all/<slug:code>/edit/', views.article_edit, name='article_edit'),
    path('all/<slug:code>/', views.article_detail, name='article_detail'),
    path('pallets/all/', views.pallets, name='pallets'),
    path('pallets/for_thermal_deburring/', views.pallets_for_thermal_deburring, name='pallets_for_thermal_deburring'),
    path('pallets/thermal_deburred/', views.pallets_thermal_deburred, name='pallets_thermal_deburred'),
    path('pallets/new/', views.pallet_new, name='pallet_new'),
    path('pallets/thermal_deburred/new/<int:pk>/', views.pallet_thermal_deburred_new, name='pallet_thermal_deburred_new'),
]
