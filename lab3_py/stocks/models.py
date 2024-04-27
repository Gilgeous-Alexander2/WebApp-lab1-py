from django.db import models

# Create your models here.


class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True) 
    second_name = models.CharField(max_length=255, blank=True, null=True)
    degree1 = models.CharField(blank=True, null=True)
    degree2 = models.CharField(blank=True, null=True)
    url = models.CharField(blank=True, null=True)

