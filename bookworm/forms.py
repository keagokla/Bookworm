from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from .models import Book, BOOK_FIELDS


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = BOOK_FIELDS
        widgets = { 'pub_date': DatePickerInput() }
