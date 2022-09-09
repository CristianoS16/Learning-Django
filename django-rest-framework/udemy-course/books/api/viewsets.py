from books.api.serializers import BooksSerializer
from books.models import Books
from rest_framework import viewsets


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
