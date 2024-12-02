from django.db import models
from car.models import Car

# Create your models here.
class Buy(models.Model):
    owned=models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    buy_date=models.DateField(auto_now_add=True)