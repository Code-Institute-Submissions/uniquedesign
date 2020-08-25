from django.urls import path
from . import views


urlpatterns = [
    path('', views.readymade, name='readymade'),
]
