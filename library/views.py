from django.shortcuts import render, get_object_or_404
from .models import  Book
from django.http import FileResponse, Http404
from django.db.models import Q


def index(request):
    sort_by = request.GET.get('sort_by')

    if sort_by == 'title':
        books = Book.objects.order_by('title')
    elif sort_by == 'author':
        books = Book.objects.order_by('author__name')
    else:
        books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'library/index.html', context)



# def read_book(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     file_url = book.file.url
#     return render(request, 'library/read_book.html', {'book': book, 'file_url': file_url})


def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        return FileResponse(book.file.open(), as_attachment=True, filename=book.file.name)
    except FileNotFoundError:
        raise Http404("File does not exist")


def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |  # Поиск по наименованию книги
            Q(author__name__icontains=query) |  # Поиск по имени автора
            Q(genre__name__icontains=query)  # Поиск по жанру
        ).distinct()  # Убираем дубликаты результатов

        context = {
            'books': books,
            'query': query
        }
    else:
        context = {}

    return render(request, 'library/book_search.html', context)
