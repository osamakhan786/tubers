from email.errors import HeaderDefect
from operator import mod
from tkinter import Button
from django.db import models

# Create your models here.

class Team(models.Model):
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    youber_link = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.frist_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    invitelink = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.headline


class Abouter(models.Model):
  
    photo = models.ImageField(upload_to='media/abouter/%Y/')



    
  
    

    