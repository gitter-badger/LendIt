from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def book(request, pk):
	book = Book.objects.filter(id=pk)[0]
	user_books = list(UserBook.objects.filter(orig_book=book))
	return render(request, 'book_page.html', {'book': book, 'userbooks': user_books})


def user_book(request, user_pk, book_pk):
	book = Book.objects.filter(id=book_pk)[0]
	lender = LenditUser.objects.filter(id=user_pk)[0]
	userbook = UserBook.objects.filter(user=lender, orig_book=book)[0]
	return render(request, 'user_book.html', {'book': userbook, 'lender': lender})


def profile(request, pk):
	lendituser = LenditUser.objects.filter(id=pk)[0]
	self_profile = request.user == lendituser.user
	user_books = UserBook.objects.filter(user=lendituser)
	return render(request, 'profile.html', {'userbooks': user_books,
											'lenuser': lendituser,
											'self_profile': self_profile})


def request_book(request, lendituser_pk, userbook_pk):
	lender = LenditUser.objects.filter(lendituser_pk)[0]
	userbook = UserBook.objects.filter(userbook_pk)[0]
	Notification(user=lender, other_user=request.user, book=userbook, type='r', desc='').save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def notifications(request):
	return render(request, 'notifications.html', {
		'notifications': Notification.objects.filter(me_user=request.user)
		})