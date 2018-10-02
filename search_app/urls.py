from django.urls import path
# . means current directory/current app
from . import views

app_name = 'search_app'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),
]
