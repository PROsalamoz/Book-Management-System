from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm, CategoryForm


def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)  # # add book to database
        if add_book.is_valid():
            add_book.save()

        add_category = CategoryForm(request.POST)  # add category to database
        if add_category.is_valid():
            add_category.save()
    else:
        book = Book.objects.all()
        categories = Category.objects.all()
        book_form = BookForm()
        category_form = CategoryForm()
        all_books = Book.objects.filter(active=True).count()
        available_books = Book.objects.filter(status='available').count()
        sold_books = Book.objects.filter(status='sold').count()
        rented_books = Book.objects.filter(status='rented').count()
        context = {
            'books': book,
            'categories': categories,
            'book_form': book_form,
            'category_form': category_form,
            'all_books': all_books,
            'available_books': available_books,
            'sold_books': sold_books,
            'rented_books': rented_books,
        }
        return render(request, 'pages/index.html', context)


def books(request):
    books = Book.objects.all()
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            books = books.filter(title__icontains=title)

    categories = Category.objects.all()
    category_form = CategoryForm()
    context = {
        'books': books,
        'categories': categories,
        'category_form': category_form,
    }
    return render(request, 'pages/book.html', context)


def update_book(request, bookId):
    book = Book.objects.get(id=bookId)
    if request.method == 'POST':
        book_data = BookForm(request.POST, request.FILES, instance=book)
        if book_data.is_valid():
            book_data.save()
            return redirect('/')

    else:
        book_data = BookForm(instance=book)
    return render(request, 'pages/update.html', context={'form': book_data})


def delete_book(request, bookId):
    book = Book.objects.get(id=bookId)
    if request.method == 'POST':
        book.delete()
        return redirect('/')

    else:
        return render(request, 'pages/delete.html', context={'book': book})


def info(request):
    return render(request, 'pages/info.html')
