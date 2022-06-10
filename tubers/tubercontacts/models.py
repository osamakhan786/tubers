from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.

class Tubercontact(models.Model):
    full_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True, default=1)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
