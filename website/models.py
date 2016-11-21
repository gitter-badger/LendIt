from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
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
    small_pic_url = models.URLField()
    email = models.EmailField()
    new_notifications = models.IntegerField(default=0)
    lat = models.DecimalField(default=0, decimal_places=3, max_digits=7)
    long = models.DecimalField(default=0, decimal_places=3, max_digits=7)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])


class UserBook(models.Model):
    STATUS = (('Lent', 'Lent'), ('Available', 'Available'))
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
    # r:request a: accept d:decline o:OTP generate
    TYPE = (('r','r'),('a','a'),('d','d'), ('o','o'), ('return','return'),('returnOTP','returnOTP'))
    user = models.ForeignKey('LenditUser', related_name='me_user')
    other_user = models.ForeignKey('LenditUser', related_name='other_user')
    book = models.ForeignKey('UserBook')
    type = models.CharField(max_length=1, choices=TYPE)
    desc = models.CharField(max_length=100, blank=True)
    read = models.IntegerField()
