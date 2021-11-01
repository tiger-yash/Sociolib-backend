from rest_framework import serializers
from authentication.models import Account
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
