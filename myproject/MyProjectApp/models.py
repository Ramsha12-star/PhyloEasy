from email import message
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.



class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(verbose_name='image', upload_to='uploaded_images/')

class Image(models.Model):
    image = models.ImageField(upload_to='img')
class details(models.Model):
    sid=models.IntegerField(null=True)
    path=models.CharField(max_length=40)


class count_check(models.Model):
    pid=models.IntegerField(null=True)