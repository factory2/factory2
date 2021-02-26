from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.departments, name='departments'),
    path('new/', views.department_new, name='department_new'),
    path('all/<slug:slug>/edit/', views.department_edit, name='department_edit'),
    path('all/<slug:slug>/', views.department_detail, name='department_detail'),
]
