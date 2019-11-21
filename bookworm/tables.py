# tutorial/tables.py
from django_tables2 import tables, TemplateColumn, Column
from django.db.models import Avg
from .models import *


class BookTable(tables.Table):
    book_review = Column(accessor='review_set',
                         verbose_name='Average rating', orderable=False)

    def render_book_review(self, value, table):
        render = '—'
        count_reviews = value.all().count()
        if count_reviews > 0:
            review_wording = 'reviews' if count_reviews > 1 else 'review'
            average_rating = value.all().aggregate(Avg('rating'))
            render = '{} {} ({} average rating)'.format(
                count_reviews, review_wording, average_rating.get('rating__avg'))
        return render

    tools_column = TemplateColumn(
        template_name='bookworm/book_tools_column.html', verbose_name='')

    summary = Column(attrs={"td": {"width": "30%"}})

    class Meta:
        model = Book
        fields = BOOK_FIELDS


class ReviewTable(tables.Table):
    tools_column = TemplateColumn(
        template_name='bookworm/review_tools_column.html', verbose_name='')

    class Meta:
        model = Review
        fields = REVIEW_FIELDS
