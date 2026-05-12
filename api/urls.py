from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryDetailView
)


urlpatterns = [
    
    # Категории
    path('category/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('category/<int:pk>/detail', CategoryDetailView.as_view(), name='category-detail-books'),
   
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
 ]