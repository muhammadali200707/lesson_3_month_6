from django.shortcuts import render
from uuid import uuid4
from book.models import Book


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/index.html', context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'book/book_detail.html', context)
