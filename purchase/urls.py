from django.urls import path
from . import views


urlpatterns = [
    path('', views.purchase, name='purchase'),
    path('add/<item_id>/', views.add_purchase, name='add_purchase'),
    path('edit/<item_id>/', views.edit_purchase, name='edit_purchase'),
    path('remove/<item_id>/', views.remove_purchase, name='remove_purchase'),
]
