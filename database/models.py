from django.db import models

class Data_set(models.Model):
    Barrel_No = models.CharField(max_length=10000)
    Barrel_type = models.CharField(max_length=10000)
    Trial_Name = models.CharField(max_length=10000)
    Plot_No = models.CharField(max_length=10000)
