from django.shortcuts import render
from .models import *


def index(request):
    book = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': book,
        'categories': categories
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
