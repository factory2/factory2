from django.urls import path

from . import views

urlpatterns = [
    path('thermal_deburrers/', views.thermal_deburrers, name='thermal_deburrers'),
    path('new/thermal_deburrer/', views.thermal_deburrer_new, name='thermal_deburrer_new'),
    path('thermal_deburrer/<int:pk>/edit/', views.thermal_deburrer_edit, name='thermal_deburrer_edit'),
    path('thermal_deburrer/<int:pk>/', views.thermal_deburrer_detail, name='thermal_deburrer_detail'),
    path('new/thermal_deburrer/basket_deburring/', views.basket_deburring_new, name='basket_deburring_new'),
    path('basket_deburring/<int:pk>/', views.basket_deburring_detail, name='basket_deburring_detail'),
    path('new/thermal_deburrer/parameter_deburring/', views.parameter_deburring_new, name='parameter_deburring_new'),
    path('parameter_deburring/<int:pk>/', views.parameter_deburring_detail, name='parameter_deburring_detail'),
]
