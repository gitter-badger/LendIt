from django.http import HttpResponse
from django.shortcuts import render, redirect
from website.models import *
import random

# Create your views here.


def home(request):
	books = list(Book.objects.all())
	random.shuffle(books)
	sixbooks = books[:6]
	return render(request, 'homepage.html', {'books': sixbooks})


def lend(request):
	if request.method == "GET":
		return render(request, 'new_lend.html', {})
	if request.method == "POST":
		name = request.POST['name']
		condition = request.POST['condition']
		desc = request.POST['desc']
		tfl = request.POST['tfl']
		url = request.POST['url']
		book = Book.objects.filter(name=name)[0]
		user = request.user
		UserBook(desc=desc, lending_time=tfl, image_url=url, condition=condition, orig_book=book, user=user).save()
		return redirect(request.META.HTTP_REFERER)


def profile(request):
	return render(request, 'profile.html', {})
