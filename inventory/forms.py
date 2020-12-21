from django.forms import ModelForm, RadioSelect
from django.utils.translation import gettext_lazy as _
from .models import Laptop

class LaptopForm(ModelForm):
  class Meta:
    model = Laptop
    fields = '__all__'
    widgets = {
      'ram': RadioSelect(),
      'processor': RadioSelect(),
      'storage_type': RadioSelect(),
      'storage_model': RadioSelect()
    }
    labels = {
      'model_type': _('Merk-Type'),
      'ram': _('RAM Capacity'),
      'storage_model': _('Storage Brand'),
      'storage_capacity': _('Storage Capacity (Gigabytes)'),
      'dvd_cd_exists': _('DVD/CD Drive'),
      'malfunction': _('Damaged or Malfunction'),
    }
    help_texts = {
      'serial_number': _('Note: Serial number can be seen from BIOS or Prompt C:. Please write down serial number on a piece of paper and put it on laptop.'),
    }