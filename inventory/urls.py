from django.urls import path
from .views import InventoryCreateView
from . import views

urlpatterns = [
  path('', InventoryCreateView.as_view(), name='inventory-home'),
]