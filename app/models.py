from django.db import models

# Create your models here.
class Dashboard(models.Model):
    Title = models.CharField(max_length=15)
    Description = models.TextField()







