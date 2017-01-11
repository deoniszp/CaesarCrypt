from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=128, verbose_name='text title')
    text = models.TextField(verbose_name='text content')

    class Meta():
        ordering = ['title']