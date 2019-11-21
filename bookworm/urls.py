from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookView.as_view(), name='books'),
    path('books/add/', BookCreateView.as_view(), name='add_book'),
    path('books/edit/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),

    path('reviews/', ReviewView.as_view(), name='reviews'),
    path('reviews/add/', ReviewCreateView.as_view(), name='add_review'),
    path('reviews/edit/<int:pk>/', ReviewUpdateView.as_view(), name='edit_review'),
    path('reviews/delete/<int:pk>/', ReviewDeleteView.as_view(), name='delete_review'),
]