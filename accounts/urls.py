from django.urls import path

from .views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('account/', TemplateView.as_view(template_name='registration/account.html'), name='account'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
