from django.db import models

# Create your models here.


class WorkSample(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=150)
