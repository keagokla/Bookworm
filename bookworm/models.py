from django.db import models
from django.urls import reverse

BOOK_FIELDS = ("title", "author", "pub_date", "summary")


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField('Publication date')
    summary = models.CharField(max_length=200, blank=True)
    
    def get_absolute_url(self):
        return reverse('books')

    def __str__(self):
        return self.title
