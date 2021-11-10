from rest_framework import serializers, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from authentication.models import Account
from .serializers import (BooksSerializer, ReviewsSerializer)
from .models import BookInfo, Reviews


class BooksView(generics.GenericAPIView):
    queryset = ''
    permission_classes = []
    serializer_class = BooksSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                serializer = BooksSerializer(BookInfo.objects.get(pk=pk))
            except:
                return Response({"non_field_errors": ["Book Does Not Exist"]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BooksSerializer(BookInfo.objects.all(), many=True)
        return Response(serializer.data)


class IssueView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        user = Account.objects.get(id=request.user.id)
        book = BookInfo.objects.get(pk=pk)
        user.books.add(book)
        user.credit-=book.price
        user.save()
        return Response(status=status.HTTP_201_CREATED)


class ReviewView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewsSerializer

    def post(self, request, pk=None):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            user=Account.objects.get(id=request.user.id)
            book = BookInfo.objects.get(pk=pk)
            is_owned=False
            if book in user.books.all():
                is_owned=True
            review=Reviews.objects.create(user=user,comment=request.data['comment'], rating=request.data['rating'],is_owned=is_owned)
            book.book_review.add(review)
            book.save()
            final_rating=0
            people=0
            for rev in book.book_review.all():
                final_rating+=rev.rating
                people+=1
            final_rating/=people
            book.rating=final_rating
            book.save()
            
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)