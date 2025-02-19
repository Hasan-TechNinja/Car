from django.db import models

# Create your models here.

class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=00)
    status = models.BooleanField(default=False)
    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE, related_name='showroom', blank=True, null=True)

    def __str__(self):
        return self.name


class Bike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name