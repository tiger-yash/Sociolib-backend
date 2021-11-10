from rest_framework import serializers
from authentication.models import Account
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from .models import BookInfo,Reviews

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields='__all__'
        depth=2

class ReviewsSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=280)
    rating = serializers.DecimalField(max_digits=2,decimal_places=1)
    class Meta:
        model=Reviews
        fields=('comment','rating')
    