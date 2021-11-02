from django.urls import path
from .views import BooksView,IssueView,ReviewView

urlpatterns = [
    path('books/', BooksView.as_view()),
    path('book/<int:pk>/', BooksView.as_view()),
    path('issue/<int:pk>/', IssueView.as_view()),
    path('review/<int:pk>/', ReviewView.as_view()),
]