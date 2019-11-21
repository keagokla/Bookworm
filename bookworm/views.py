from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Review
from .tables import BookTable, ReviewTable
from .forms import BookForm, ReviewForm


class BookView(LoginRequiredMixin, SingleTableView):
    model = Book
    table_class = BookTable
    template_name_suffix = '_list'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        """Detect the submit button used and act accordingly"""
        url_name = 'add_book' if 'add_another_book' in self.request.POST else 'books'
        return reverse_lazy(url_name)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('books')


class ReviewView(LoginRequiredMixin, SingleTableView):
    model = Review
    table_class = ReviewTable
    template_name_suffix = '_list'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name_suffix = '_create_form'

    def get_success_url(self):
        """Detect the submit button used and act accordingly"""
        url_name = 'add_review' if 'add_another_review' in self.request.POST else 'reviews'
        return reverse_lazy(url_name)
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name_suffix = '_update_form'


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    form_class = ReviewForm
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('reviews')
