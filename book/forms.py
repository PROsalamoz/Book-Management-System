from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_image',
            'author_image',
            'pages',
            'price',
            'price_for_rent',
            'rent_period',
            'total_rented_price',
            'status',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control'}),
            'author_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_for_rent': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rented_price'}),
            'rent_period': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rented_period'}),
            'total_rented_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_rented_price'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
