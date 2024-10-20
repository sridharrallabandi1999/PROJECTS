import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library_management.settings")
django.setup()

from books.models import Book

# List of books
book_data = [
    {"title": "The Intelligent Investor", "author": "Benjamin Graham", "genre": "Stock Market", "stock": 10},
    {"title": "A Random Walk Down Wall Street", "author": "Burton G. Malkiel", "genre": "Stock Market", "stock": 5},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Self-Help", "stock": 8},
    {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "genre": "Self-Help", "stock": 12},
    # Add more books here...
]

# Populate database
for book in book_data:
    Book.objects.create(**book)

print("Books added successfully!")
