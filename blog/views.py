from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView
)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import Post, Categoria
from .serializers import (
    PostSerializer, UserSerializer, PostDetailSerializer, CategoriaSerializer
)


# 🔥 Vista para Listar y Crear Posts
class PostList(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-fecha_publicacion')
    serializer_class = PostSerializer


# 🔥 Detalle de un Post por slug
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


# 🔥 Vista para Listar y Crear Categorías
class CategoriaList(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# 🔥 Vista para Filtrar Posts por Categoría
class CategoriaDetailAPIView(ListAPIView):
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        categoria_id = self.request.query_params.get('categoria', None)
        if categoria_id:
            return Post.objects.filter(categoria=categoria_id).order_by('-fecha_publicacion')
        return Post.objects.all().order_by('-fecha_publicacion')


# 🔥 Registro de usuarios
class UserCreate(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


# 🔥 Login (retorna el token si las credenciales son correctas)
class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response(
                {"error": "Credenciales incorrectas"},
                status=status.HTTP_400_BAD_REQUEST
            )
