from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book-list'),
    path('book_detail/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author-list'),
    path('author_detail/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
