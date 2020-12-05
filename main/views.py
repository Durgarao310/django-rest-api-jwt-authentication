from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
