import email
from django.db import models
from distutils.command.upload import upload
from unicodedata import category, name
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class linker(models.Model):
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    twiter = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    