from django.db import models

# The Author model represents a writer who can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)  # The name of the author

    def __str__(self):
        return self.name  # Returns the author's name as a string representation

# The Book model represents a book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # The title of the book
    publication_year = models.IntegerField()  # The year the book was published
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # One-to-many relationship: an author can have multiple books

    def __str__(self):
        return f"{self.title} ({self.publication_year})"  # Returns the book's title and year
