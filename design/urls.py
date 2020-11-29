from django.urls import path
from . import views


urlpatterns = [
    path('', views.design, name='design'),
    path('<int:product_id>/', views.design_detail, name='design_detail'),
    path('add/', views.add_design, name='add_design'),
    path('update/<int:product_id>/', views.update_design, name='update_design'),
]
