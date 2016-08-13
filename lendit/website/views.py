from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'homepage.html', {})


def lend(request):
	return render(request, 'new_lend.html', {})

def book(request):
	return render(request, 'book_page.html', {})
