from django.db import models

class Cv(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'pictures',default = None)
