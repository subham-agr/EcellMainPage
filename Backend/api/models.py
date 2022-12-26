from django.db import models

# Create your models here.
class Home(models.Model):
    about = models.CharField(max_length=3000,blank=True)
    about_image = models.ImageField(blank=True)

class Initiatives(models.Model):
    initiative_id = models.CharField(max_length=20,blank=True)
    initiative_name = models.CharField(max_length=300,blank=True)
    coverimage = models.ImageField(blank=True)
    introtext = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.initiative_name

class HomeCoverImage(models.Model):
    sequence = models.IntegerField(blank=True)
    image_name = models.CharField(max_length=300,blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.image_name