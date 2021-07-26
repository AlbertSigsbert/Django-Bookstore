from django.shortcuts import render
# import json
from book.models import Book
# Create your views here.

# Load books from JSON file


def index(request):
    # with open('bookstore/books.json') as file:
    #     books = json.load(file)
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'books/index.html', context)


def show(request, id):
    # with open('bookstore/books.json') as file:
    #     book_dict = json.load(file)['books']

    # book = [book for book in book_dict if book['id'] == id]
    # context = {'book': book[0]}

    book = Book.objects.get(pk=id)

    context = {'book': book}

    return render(request, 'books/show.html', context)
