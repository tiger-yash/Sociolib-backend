from rest_framework import serializers, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.models import Account
from .serializers import ()

def create_auth_token(user):
    token, _ = Token.objects.get_or_create(user=user)
    return token

# class RegisterView(generics.CreateAPIView):


# class LoginView(generics.GenericAPIView):


# class ProfileView(generics.GenericAPIView):