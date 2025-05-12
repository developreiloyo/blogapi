from rest_framework import serializers
from .models import Post, Autor, Categoria
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields= '__all__'

class AutorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Autor
            fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('username','email', 'password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validate_data):
        user = User(
            email = validate_data['email'],
            username =validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user) 
        return user
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image