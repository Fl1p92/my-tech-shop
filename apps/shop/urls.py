from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index')
]