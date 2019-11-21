from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

BOOK_FIELDS = ("title", "author", "pub_date", "summary")
REVIEW_FIELDS = ("book", "rating", "comment", "created_by")
CHAR_FIELD_LENGTH = 150


class Book(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_LENGTH)
    author = models.CharField(max_length=CHAR_FIELD_LENGTH)
    pub_date = models.DateField('Publication date')
    summary = models.CharField(max_length=CHAR_FIELD_LENGTH, blank=True)

    def get_absolute_url(self):
        return reverse('books')

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.CharField(max_length=CHAR_FIELD_LENGTH)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="reviewed by", default="")

    def get_absolute_url(self):
        return reverse('reviews')

    def __str__(self):
        return self.book.title
