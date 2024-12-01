from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# The BookSerializer serializes data for the Book model.
# It validates that the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer serializes data for the Author model.
# It includes a nested BookSerializer to display the author's books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
