from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length= 20)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

# Create your models here.



