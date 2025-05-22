from django.urls import path
from .views import (
    PostList,
    PostDetailAPIView,
    CategoriaList,
    CategoriaDetailAPIView,
    UserCreate,
    LoginView,
)

urlpatterns = [
    path('post/', PostList.as_view(), name='post_list'),
    path('postdetail/<slug:slug>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('categorias/', CategoriaList.as_view(), name='categoria_list'),
    path('posts-by-categoria/', CategoriaDetailAPIView.as_view(), name='posts_by_categoria'),
    path('usuarios/', UserCreate.as_view(), name='usuario_crear'),
    path('login/', LoginView.as_view(), name='login'),
]
