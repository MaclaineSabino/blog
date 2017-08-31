from rest_framework import serializers
from postagens.models import *

class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = ('url',
                  'pk',
                  'lat',
                  'lng')



class AddressSerializer(serializers.ModelSerializer):



    class Meta:
        model = Address
        fields = (
            'url',
            'pk',
            'street',
            'suite',
            'city',
            'zipcode',
            'geo',
            'users'
        )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

    class Meta:
        model = Comment
        fields = (
            'url',
            'name',
            'email',
            'body',
            'post',

        )


class PostSerializerComentarios(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    #comentarios_do_post = CommentSerializer   #-- deixando assim resopnde a letra F
    comentarios_do_post = CommentSerializer(
        many=True,
        read_only=True

     )

    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'body',
            'user',
            'comentarios_do_post'

        )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')



    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'body',
            'user'


        )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'name',
            'username',
            'email',
            'posts',
        )
