from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = BOOK_FIELDS
        widgets = {'pub_date': DatePickerInput()}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = REVIEW_FIELDS[:-1]
        widgets = {
        'created_by': forms.TextInput(attrs={'readonly': True}),
    }
