
from django.conf import settings
from django.urls import path

from .views import home_view, list_view, main_view

urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_view, name='home'),
    path('list/', list_view, name='list'),
]
