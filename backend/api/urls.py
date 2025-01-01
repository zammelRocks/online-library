from django.urls import path
from .views import (
    CreateUserView, UserListView, UserDetailView,
    CategoryListCreateView, CategoryDetailView,
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView,
    ResearchPaperListCreateView, ResearchPaperDetailView,
    ArticleListCreateView, ArticleDetailView,
    BorrowListCreateView, BorrowDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    # User URLs
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # ResearchPaper URLs
    path('researchpapers/', ResearchPaperListCreateView.as_view(), name='researchpaper-list-create'),
    path('researchpapers/<int:pk>/', ResearchPaperDetailView.as_view(), name='researchpaper-detail'),

    # Article URLs
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),

    # Borrow URLs
    path('borrows/', BorrowListCreateView.as_view(), name='borrow-list-create'),
    path('borrows/<int:pk>/', BorrowDetailView.as_view(), name='borrow-detail'),

    # Review URLs
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
