from django.urls import path
from . import views


urlpatterns = [
    path('', views.design, name='design'),
]
