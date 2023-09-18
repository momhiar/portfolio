from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class WorkSampleImage(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    alt = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='work-samples')

    def __str__(self):
        return self.title


class WorkSampleTag(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class WorkSample(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=150)
    text = tinymce_models.HTMLField()
    gallery = models.ManyToManyField(WorkSampleImage)
    tags = models.ManyToManyField(WorkSampleTag)

    def __str__(self):
        return self.title
