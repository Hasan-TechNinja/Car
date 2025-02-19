from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=00)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    

class Bike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name