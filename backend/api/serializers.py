from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Author, Book, ResearchPaper, Article, Borrow, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        #print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]

 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id", "id_mdh", "cote", "inventaire", "opn", "titre", "auteurs",
            "lieu_ed", "suif_notes", "public_notes", "isbn_a", "isbn_c",
            "form_doss", "s265b", "specialite", "nb_page", "date_edition",
            "editeur", "prix"
        ]



class ResearchPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = [
            "id", "id_mdh", "cote", "inventaire", "opn", "titre", "auteurs",
            "lieu_ed", "suif_notes", "public_notes", "isbn_a", "isbn_c",
            "form_doss", "s265b", "specialite", "nb_page", "date_edition",
            "editeur", "prix"
        ]

  

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id", "id_mdh", "cote", "inventaire", "opn", "titre", "auteurs",
            "lieu_ed", "suif_notes", "public_notes", "isbn_a", "isbn_c",
            "form_doss", "s265b", "specialite", "nb_page", "date_edition",
            "editeur", "prix"
        ]

    

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ["id", "user", "book", "borrow_date", "return_date"]
        read_only_fields = ["borrow_date"]

  

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id", "user", "book", "research_paper", "article", "rating",
            "comment", "created_at"
        ]
        read_only_fields = ["created_at"]

