from django.urls import path
from .views import (FriendView,SearchView,FriendCreationView)

urlpatterns = [
    path('<int:pk>/', FriendView.as_view()),
    path('search/', SearchView.as_view()),
    path('/req/<int:pk>/', FriendCreationView.as_view()),
]
