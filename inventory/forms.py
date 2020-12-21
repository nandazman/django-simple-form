from django import forms

class Laptop(models.Model):
  
  class Type(models.TextChoices):
    HP_PRO_BOOK = 'HP-ProBook', _('HP-ProBook')
    HP_COMPAQ = 'HP-Compaq', _('HP-Compaq')
    HP_ELITEBOOK = 'HP-Elitebook', _('HP-Elitebook')
    ASUS_N46VM = 'Asus-N46VM', _('Asus-N46VM')
    LENOVO_THINKPAD = 'Lenovo-Thinkpad', _('Lenovo-Thinkpad')
  
  class Processor(models.TextChoices):
    I3 = 'I3', _('I3')
    I5 = 'I5', _('I5')
    I7 = 'I7', _('I7')
  
  class RAM(models.TextChoices):
    GB4 = '4GB', _('4GB')
    GB6 = '6GB', _('6GB')
    GB8 = '8GB', _('8GB')
    GB12 = '12GB', _('12GB')
    GB16 = '16GB', _('16GB')
  
  class StorageType(models.TextChoices):
    HDD = 'HDD', _('HDD')
    SSD = 'SSD', _('SSD')
  
  class StorageModel(models.TextChoices):
    HITACHI = 'Hitachi (HGST)', _('Hitachi (HGST)')
    WD = 'WD (Westernd Digital)', _('WD (Westernd Digital)')
    SEAGATE = 'Seagate', _('Seagate')
    TOSHIBA = 'Toshiba', _('Toshiba')
    OCZ = 'OCZ Vertex', _('OCZ Vertex')
    SAMSUNG = 'Samsung 860 Vevo', _('Samsung 860 Vevo')

  model_type = forms.CharField(label='Address', choices=Type.choices)
  
  serial_number = models.CharField()
  processor = models.CharField(choices=Processor.choices)
  ram = models.CharField(choices=RAM.choices)
  storage_type = models.CharField(choices=StorageType.choices)
  
  storage_model = models.CharField(choices=StorageModel.choices)
  
  storage_capacity = models.PositiveIntegerField()
  dvd_cd_exists = models.BooleanField(default=False)