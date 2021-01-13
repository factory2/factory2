from django.urls import path
from . import views

urlpatterns = [
    path('articles_thermal_deburring', views.articles_thermal_deburring, name='articles_thermal_deburring'),
    path('articles_thermal_deburring/<slug:article_code>', views.article_thermal_deburring_detail, name='article_thermal_deburring_detail'),
    path('article_thermal_deburring/new/', views.article_thermal_deburring_new, name='article_thermal_deburring_new'),
    path('article_thermal_deburring/<slug:article_code>/edit/', views.article_thermal_deburring_edit, name='article_thermal_deburring_edit'),
    path('pallet_thermal_deburred/new/', views.pallet_thermal_deburred_new, name='pallet_thermal_deburred_new'),
]
