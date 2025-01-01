from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    id_mdh = models.CharField(max_length=50, unique=True)
    cote = models.CharField(max_length=50, blank=True, null=True)
    inventaire = models.CharField(max_length=50, blank=True, null=True)
    opn = models.CharField(max_length=50, blank=True, null=True)
    titre = models.CharField(max_length=255)
    auteurs = models.ManyToManyField(Author, related_name='books')
    lieu_ed = models.CharField(max_length=255, blank=True, null=True)
    suif_notes = models.TextField(blank=True, null=True)
    public_notes = models.TextField(blank=True, null=True)
    isbn_a = models.CharField(max_length=50, blank=True, null=True)
    isbn_c = models.CharField(max_length=50, blank=True, null=True)
    form_doss = models.CharField(max_length=255, blank=True, null=True)
    s265b = models.CharField(max_length=50, blank=True, null=True)
    specialite = models.CharField(max_length=255, blank=True, null=True)
    nb_page = models.PositiveIntegerField(blank=True, null=True)
    date_edition = models.DateField(blank=True, null=True)
    editeur = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.titre

class ResearchPaper(models.Model):
    id_mdh = models.CharField(max_length=50, unique=True)
    cote = models.CharField(max_length=50, blank=True, null=True)
    inventaire = models.CharField(max_length=50, blank=True, null=True)
    opn = models.CharField(max_length=50, blank=True, null=True)
    titre = models.CharField(max_length=255)
    auteurs = models.ManyToManyField(Author, related_name='research_papers')
    lieu_ed = models.CharField(max_length=255, blank=True, null=True)
    suif_notes = models.TextField(blank=True, null=True)
    public_notes = models.TextField(blank=True, null=True)
    isbn_a = models.CharField(max_length=50, blank=True, null=True)
    isbn_c = models.CharField(max_length=50, blank=True, null=True)
    form_doss = models.CharField(max_length=255, blank=True, null=True)
    s265b = models.CharField(max_length=50, blank=True, null=True)
    specialite = models.CharField(max_length=255, blank=True, null=True)
    nb_page = models.PositiveIntegerField(blank=True, null=True)
    date_edition = models.DateField(blank=True, null=True)
    editeur = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.titre

class Article(models.Model):
    id_mdh = models.CharField(max_length=50, unique=True)
    cote = models.CharField(max_length=50, blank=True, null=True)
    inventaire = models.CharField(max_length=50, blank=True, null=True)
    opn = models.CharField(max_length=50, blank=True, null=True)
    titre = models.CharField(max_length=255)
    auteurs = models.ManyToManyField(Author, related_name='articles')
    lieu_ed = models.CharField(max_length=255, blank=True, null=True)
    suif_notes = models.TextField(blank=True, null=True)
    public_notes = models.TextField(blank=True, null=True)
    isbn_a = models.CharField(max_length=50, blank=True, null=True)
    isbn_c = models.CharField(max_length=50, blank=True, null=True)
    form_doss = models.CharField(max_length=255, blank=True, null=True)
    s265b = models.CharField(max_length=50, blank=True, null=True)
    specialite = models.CharField(max_length=255, blank=True, null=True)
    nb_page = models.PositiveIntegerField(blank=True, null=True)
    date_edition = models.DateField(blank=True, null=True)
    editeur = models.CharField(max_length=255, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.titre


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    research_paper = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username}"

