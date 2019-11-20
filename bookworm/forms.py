from django.forms import ModelForm
from .models import Book, BOOK_FIELDS


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = BOOK_FIELDS
