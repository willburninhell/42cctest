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


class RequestLog(models.Model):
    date = models.DateTimeField('Request date and time')
    method = models.CharField(max_length=7)
    url = models.CharField(max_length=256)
    query_str = models.CharField(max_length=256,default="?")
