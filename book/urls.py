from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('update/<int:bookId>', views.update_book, name='updateBook'),
    path('delete/<int:bookId>', views.delete_book, name='deleteBook'),
    path('info', views.info, name='info'),
]
