from django.db import models

# Create your models here.
class Page(models.Model):
    pageText = models.CharField(max_length=120)