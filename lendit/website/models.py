from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=20)


class LenditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_pic_url = models.URLField()
    email = models.EmailField()


class UserBook(models.Model):
    STATUS = (('lent', 'lent'), ('unlent','unlent'))
    user = models.ForeignKey('LenditUser')
    orig_book = models.ForeignKey('Book')
    desc = models.CharField(max_length=1000)
    condition = models.CharField(max_length=100)
    lending_time = models.IntegerField()
    image_url = models.URLField()
    status = models.CharField(max_length=10, choices=STATUS)


class RequestSent(models.Model):
    user = models.ForeignKey('LenditUser')
    lender = models.IntegerField()
    book = models.CharField(max_length=255)


class Notification(models.Model):
    TYPE = (('r','r'),('a','a'),('d','d'))
    user = models.ForeignKey('LenditUser')
    other_user = models.IntegerField()
    book_id = models.IntegerField()
    type = models.CharField(max_length=1, choices=TYPE)
    desc = models.CharField(max_length=100, blank=True)

