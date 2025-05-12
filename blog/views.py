from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,ListCreateAPIView
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response  
from .models import Post, Categoria
from .serializers import PostSerializer, UserSerializer, PostDetailSerializer, CategoriaSerializer
from django.contrib.auth import authenticate
from .pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination,
)
from .helper import *

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserCreate(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = ()
 
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(RetrieveAPIView):
    permission_classes = ()
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    # lookup_url_kwarg = 'abc'

class CategoriaList(ListCreateAPIView):
    permission_classes = ()
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # lookup_url_kwarg = 'abc'

class CategoriaDetailAPIView(ListAPIView):
    permission_classes = ()
    queryset = Post.objects.all().filter()
    serializer_class = PostDetailSerializer
    filterset_fields = ['categoria']#

class TagsCisco(ListAPIView):
    permission_classes = ()
    queryset = categoria(1)
    serializer_class = PostDetailSerializer

	
class TagsPython(ListAPIView):
    permission_classes = ()
    queryset = categoria(2)
    serializer_class = PostDetailSerializer	