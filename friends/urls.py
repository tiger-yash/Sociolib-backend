from django.urls import path
from .views import (FriendView,SearchView,FriendCreationView,AllFriendsView,AllRequestsView)

urlpatterns = [
    path('<int:pk>/', FriendView.as_view()),
    path('search/', SearchView.as_view()),
    path('req/<int:pk>/', FriendCreationView.as_view()),
    path('all/', AllFriendsView.as_view()),
    path('requests/', AllRequestsView.as_view()),
]
