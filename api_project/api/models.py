from django.db import models


from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # A CharField for the book title
    author = models.CharField(max_length=255)  # A CharField for the book author

    def __str__(self):
        return f"{self.title} by {self.author}"  # String representation for the model
