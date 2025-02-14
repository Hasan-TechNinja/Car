from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name