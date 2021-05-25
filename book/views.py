from django.shortcuts import render
from .models import *
from .forms import BookForm


def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

    book = Book.objects.all()
    categories = Category.objects.all()
    book_form = BookForm()
    context = {
        'books': book,
        'categories': categories,
        'book_form': book_form
    }
    return render(request, 'pages/index.html', context)


def books(request):
    book = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': book,
        'categories': categories
    }
    return render(request, 'pages/book.html', context)
