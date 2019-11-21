# tutorial/tables.py
from django_tables2 import tables, TemplateColumn, Column
from .models import Book, BOOK_FIELDS


class BookTable(tables.Table):
    tools_column = TemplateColumn(
        template_name='bookworm/tools_column.html', verbose_name='')
    
    summary = Column(attrs={"td": {"width": "40%"}})

    class Meta:
        model = Book
        fields = BOOK_FIELDS
