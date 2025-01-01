# api/admin.py

from django.contrib import admin
from .models import  Category, Author, Book, ResearchPaper, Article, Borrow, Review


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(ResearchPaper)
admin.site.register(Article)
admin.site.register(Borrow)
admin.site.register(Review)
