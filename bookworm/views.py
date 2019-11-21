from django_tables2 import SingleTableView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .tables import BookTable
from .forms import BookForm


class BookView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name_suffix = '_list'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_create_form'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'


class BookDeleteView(DeleteView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('books')
