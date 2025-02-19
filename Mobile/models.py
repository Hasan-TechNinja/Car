from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name
    

class Mobile(models.Model):
    model_name = models.CharField(max_length=255)
    display = models.FloatField()
    battery_capacity = models.CharField(default="00 Mh", max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')

    def __str__(self):
        return f"{self.brand}, {self.model_name}"