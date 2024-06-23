from django import forms
from .models import Author, Book, Genre

from django import forms
from .models import Author, Book, Genre


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'genre', 'author', 'photo_book', 'file']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
