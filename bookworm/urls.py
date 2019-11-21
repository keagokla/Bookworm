from django.urls import path
from django.views.generic import RedirectView
from .views import BookView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='books', permanent=True)),

    path('books/', BookView.as_view(), name='books'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('books/edit/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),
]