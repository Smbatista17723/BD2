
from django.db import models

class UtiModel(models.Model):
    desig=models.CharField(max_length = 100)
    passwd=models.CharField(max_length = 100)
    class Meta:
        db_table="utilizadores"