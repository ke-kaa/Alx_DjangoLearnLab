import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    publication_year = django_filters.NumberFilter(lookup_expr='exact', label='Publication Year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
