from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import (FriendSerializer)
from authentication.models import Account
from friends.models import FriendList,FriendRequest

class FriendView(generics.GenericAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class = FriendSerializer

    ### TO GET SPECIFIC USER DATA
    def get(self,request,pk):
        try:
            serializer=FriendSerializer(Account.objects.get(id=pk))
            data=serializer.data
            person=Account.objects.get(pk=pk)
            friend_status(data,request,person)
            return Response(data)
        except:
            return Response({"non_field_errors":["User Does Not Exist"]},status=status.HTTP_400_BAD_REQUEST)

    ### TO SEND FRIEND REQUEST
    def post(self,request,pk):
        try:
            serializer=FriendSerializer(Account.objects.get(id=pk))
            data=serializer.data
            person=Account.objects.get(id=pk)
            sender=Account.objects.get(username=request.user)
            
            try:
                friend_req=FriendRequest.objects.get(sender=sender,receiver=person)
                friend_req.is_active=True
                friend_req.save(update_fields=['is_active'])
            except:
                FriendRequest.objects.create(sender=request.user,receiver=person)
            data["request_sent"]=True
            return Response(data,status=status.HTTP_201_CREATED)
        except:
            return Response({"non_field_errors":["Request Could not be Sent. Try Again Later!"]},status=status.HTTP_408_REQUEST_TIMEOUT)

    ### TO CANCEL SENT REQUEST
    def patch(self,request,pk):
        try:
            serializer=FriendSerializer(Account.objects.get(id=pk))
            data=serializer.data
            person=Account.objects.get(id=pk)
            obj=FriendRequest.objects.get(sender=request.user,receiver=person)
            obj.cancel()
            data["request_sent"]=False
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({"non_field_errors":["Request Could not be UnSent. Try Again Later!"]},status=status.HTTP_408_REQUEST_TIMEOUT)

    ### TO UNFRIEND
    def delete(self,request,pk): 
        try:
            serializer=FriendSerializer(Account.objects.get(id=pk))
            data=serializer.data
            person=Account.objects.get(id=pk)
            obj=FriendList.objects.get(user=request.user)
            obj.unfriend(person)
            data["is_friend"]=False
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({"non_field_errors":["Request Could not be UnSent. Try Again Later!"]},status=status.HTTP_408_REQUEST_TIMEOUT)

class SearchView(generics.GenericAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class = FriendSerializer

    ### TO SEARCH FOR USERS
    def get(self,request):
        get_data=request.data['username'].strip()
        if get_data:
            users=Account.objects.filter(username__icontains=get_data)
        else:
            users=Account.objects.all()
        serializer=FriendSerializer(users,many=True)
        data=serializer.data
        for user in data:
            person=Account.objects.get(pk=user['id'])
            friend_status(user,request,person)
        return  Response(data,status=status.HTTP_200_OK)

class FriendCreationView(generics.GenericAPIView):   
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class = FriendSerializer
    queryset=""
    
    ### TO ACCEPT Friend Request
    def post(self,request,pk):
        try:
            serializer=FriendSerializer(Account.objects.get(pk=pk))
            person=Account.objects.get(id=pk)
            obj=FriendRequest.objects.get(sender=person,receiver=request.user)
            obj.accept()
            data=serializer.data
            friend_status(data,request,person)
            return Response(data,status=status.HTTP_201_CREATED)
        except:
            return Response({"non_field_errors":["User Does Not Exist"]},status=status.HTTP_400_BAD_REQUEST)

    ### TO DECLINE Friend Request
    def delete(self,request,pk):
        try:
            serializer=FriendSerializer(Account.objects.get(pk=pk))
            person=Account.objects.get(id=pk)
            obj=FriendRequest.objects.get(sender=person,receiver=request.user)
            obj.decline()
            data=serializer.data
            friend_status(data,request,person)
            return Response(data,status=status.HTTP_201_CREATED)
        except:
            return Response({"non_field_errors":["User Does Not Exist"]},status=status.HTTP_400_BAD_REQUEST)

def friend_status(user,request,person): 
        try:
            FriendList.objects.get(user=request.user,friends=person)
            friend=True
        except:
            friend=False
        try:
            FriendRequest.objects.get(sender=request.user,receiver=person,is_active=True)
            sent=True
        except:
            sent=False
        try:
            FriendRequest.objects.get(sender=person,receiver=request.user,is_active=True)
            received=True
        except:
            received=False
        if request.user==person:
            user["is_self"]=True
        elif friend:
            user["is_friend"]=True
        elif sent:
            user["request_sent"]=True
        elif received:
            user["request_received"]=True
