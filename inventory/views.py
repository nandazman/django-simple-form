from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Laptop
from .forms import LaptopForm

class InventoryCreateView(SuccessMessageMixin, CreateView):
  model = Laptop
  form_class = LaptopForm
  success_message = "Created successfully"


  def get_success_message(self, cleaned_data):
    return self.success_message % dict(
      cleaned_data
    )
