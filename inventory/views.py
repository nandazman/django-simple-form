from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Laptop

class InventoryCreateView(SuccessMessageMixin, CreateView):
  model = Laptop
  fields = ['model_type', 'serial_number', 'processor', 'ram', 'storage_type', 'storage_model', 'storage_capacity', 'dvd_cd_exists', 'malfunction']
  success_message = "Created successfully"

  # def form_valid(self, form):
  #   return super().form_valid(form)
  
  def get_success_message(self, cleaned_data):
    messages.add_message(self.request, messages.INFO, 'Hello world.')
    return self.success_message % dict(
      cleaned_data
    )
