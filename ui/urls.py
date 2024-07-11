# ui/urls.py
from django.urls import path
from .views import home, search, results

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('results/', results, name='results'),
]
