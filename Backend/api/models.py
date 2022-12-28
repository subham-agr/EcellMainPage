from django.db import models

# Create your models here.
HEADING_CHOICES =(
    ("Events & PR Head","Events & PR Head"),
    ("Marketing Head","Marketing Head"),
    ("Design Head","Design Head"),
    ("Technical & Web Head","Technical & Web Head"),
    ("Corporate Relations Head","Corporate Relations Head"),
    ("Media Head","Media Head"),
    ("Operations Head","Operations Head"),
    ("Overall Coordinator","Overall Coordinator"),
)

class HeadingTeam(models.Model):
    heading = models.CharField(max_length=300, choices=HEADING_CHOICES, default= '1',blank=True)

    def __str__(self):
        return self.heading

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
    heading = models.ForeignKey(HeadingTeam, on_delete=models.CASCADE,blank=True, default=True)
    name = models.CharField(max_length=300, blank=True)
    designation = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True)
    linkedin = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    whatsapp = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)