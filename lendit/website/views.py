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
		lendituser = LenditUser.objects.filter(user=request.user)[0]
		UserBook(desc=desc, lending_time=tfl, image_url=url, condition=condition, orig_book=book, user=lendituser).save()
		return HttpResponse("asdfas")


def book(request, pk):
	book = Book.objects.filter(id=pk)[0]
	user_books = list(UserBook.objects.filter(orig_book=book))
	return render(request, 'book_page.html', {'book': book, 'userbooks':user_books})


def profile(request, pk):
	lendituser = LenditUser.objects.filter(id=pk)[0]
	user_books = UserBook.objects.filter(user=lendituser)
	return render(request, 'profile.html', {'userbooks': user_books, 'lenuser': lendituser})