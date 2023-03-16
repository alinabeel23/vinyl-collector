from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class RecordPlayer (models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recordplayers_detail', kwargs={'pk': self.id})
    

class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year_released = models.IntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='main_app/static/uploads/', default ="")

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'vinyl_id':self.id})


