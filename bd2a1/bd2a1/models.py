
from django.db import models

class Enc(models.Model):
    e_id = models.IntegerField()
    data = models.DateField()
    email = models.CharField(max_length=100)
    preço = models.FloatField()