from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField("date of birth")
    bio = models.TextField(default="", blank=True)
    email = models.EmailField(max_length=64)
    jabber = models.EmailField(max_length=64)
    skype = models.CharField(max_length=64)
    other = models.TextField(default="", blank=True)
