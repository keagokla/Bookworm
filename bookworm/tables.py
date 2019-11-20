# tutorial/tables.py
import django_tables2 as tables
from .models import Book, BOOK_FIELDS


class BookTable(tables.Table):
    tools_column = tables.TemplateColumn(
        template_name='bookworm/tools_column.html', verbose_name='')
    
    summary = tables.Column(attrs={"td": {"width": "50%"}})

    class Meta:
        model = Book
        fields = BOOK_FIELDS
