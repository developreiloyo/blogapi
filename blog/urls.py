from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import PostList, UserCreate, LoginView, PostDetailAPIView, CategoriaList,CategoriaDetailAPIView, TagsCisco, TagsPython

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('v1/post/', PostList.as_view(),name='post_list' ),
    path('v1/postdetail/<slug:slug>', PostDetailAPIView.as_view(),name='post_detail' ),
    path('v1/usuarios/', UserCreate.as_view(),name='usuario_crear' ),

    path('v1/categorias/cisco', TagsCisco.as_view(),name='categoria_list_Cisco' ),
    path('v1/categorias/python', TagsPython.as_view(),name='categoria_list_Python' ),
    ]

# Para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
]'''