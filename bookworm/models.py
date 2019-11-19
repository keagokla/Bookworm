from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_year = models.DateField('year of publishing')
    summary = models.CharField(max_length=200)

    def __str__(self):
            return self.title
