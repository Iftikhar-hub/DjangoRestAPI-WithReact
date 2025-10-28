from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"