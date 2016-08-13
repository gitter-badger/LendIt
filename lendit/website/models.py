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
    profile_pic_url = models.URLField()
    email = models.EmailField()


class UserBook(models.Model):
    STATUS = (('Lent', 'Lent'), ('Available','Available'))
    user = models.ForeignKey('LenditUser')
    orig_book = models.ForeignKey('Book')
    desc = models.CharField(max_length=1000)
    condition = models.CharField(max_length=100)
    lending_time = models.IntegerField()
    image_url = models.URLField()
    status = models.CharField(max_length=10, choices=STATUS, default="Available")


class Borrowed(models.Model):
    user = models.ForeignKey('LenditUser', related_name='borrower') 
    lender = models.ForeignKey('LenditUser', related_name='lender')
    book = models.ForeignKey('UserBook')
    accepted = models.IntegerField()


class Notification(models.Model):
    TYPE = (('r','r'),('a','a'),('d','d'))
    user = models.ForeignKey('LenditUser', related_name='me_user')
    other_user = models.ForeignKey('LenditUser', related_name='other_user')
    book = models.ForeignKey('UserBook')
    type = models.CharField(max_length=1, choices=TYPE)
    desc = models.CharField(max_length=100, blank=True)
    read = models.IntegerField()
