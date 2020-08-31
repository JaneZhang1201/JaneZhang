from django.db import models

class Feedback(models.Model):
    user_name  = models.CharField('name',max_length=120)
    evaluation = models.BooleanField('I like this page！', null = True)
    email      = models.EmailField('email',blank=True)
    message    = models.TextField('advice',max_length=120)
# Create your models here.
