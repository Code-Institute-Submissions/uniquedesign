from django.urls import path
from . import views


urlpatterns = [
    path('', views.design, name='design'),
    path('<product_id>', views.design_detail, name='design_detail'),
]
