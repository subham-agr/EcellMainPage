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

class Gallery(models.Model):
    sequence = models.IntegerField(blank=True)
    image_name = models.CharField(max_length=300,blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.image_name

class Patronages(models.Model):
    sequence = models.IntegerField(blank=True)
    image_name = models.CharField(max_length=300,blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.image_name

class Vision(models.Model):
    vision = models.CharField(max_length=1000,blank=True)
    vision_image = models.ImageField(blank=True)

class Team(models.Model):
    name = models.CharField(max_length=300, blank=True)
    designation = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True)
    linkedin = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    whatsapp = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)