from django.db import models

class ESW(models.Model):
    name = models.CharField(max_length=100)
