from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
