from rest_framework import serializers
from authentication.models import Account
from friends.models import FriendList,FriendRequest


class FriendSerializer(serializers.ModelSerializer):
    is_self=serializers.BooleanField(default=False)
    is_friend=serializers.BooleanField(default=False)
    request_sent=serializers.BooleanField(default=False)
    request_received=serializers.BooleanField(default=False)
    class Meta:
        model=Account
        fields=('id','username','is_self','is_friend','request_sent','request_received')

class AllFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FriendList
        fields='__all__'
        depth=2