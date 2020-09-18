from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('add/<item_id>', views.add_purchase, name='add_purchase'),
]
