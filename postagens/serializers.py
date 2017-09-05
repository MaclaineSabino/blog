from rest_framework import serializers
from postagens.models import *
from django.contrib.auth.models import User


class GeoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Geo
        fields = (
                  'lat',
                  'lng')





class AddressSerializer(serializers.ModelSerializer):

    geo = GeoSerializer(read_only=True)


    class Meta:
        model = Address
        fields = (

            'pk',
            'street',
            'suite',
            'city',
            'zipcode',
            'geo'



        )




class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

    class Meta:
        model = Comment
        fields = (
            'url',
            'pk',
            'name',
            'email',
            'body',
            'post',

        )


class PostSerializerComentarios(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
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
            'owner',
            'comentarios_do_post'

        )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')




    class Meta:
        model = Post
        fields = (
            'url',
            'owner',
            'title',
            'body',



        )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    postss = PostSerializer

    address = AddressSerializer(

        read_only=True

     )

    class Meta:
        model = Usuario
        fields = (

            'pk',
            'name',
            'username',
            'email',
            'address',
            'postss',
        )


class UserSerializerDetail(serializers.HyperlinkedModelSerializer):
    postss = PostSerializer

    address = AddressSerializer(

        read_only=True

     )

    class Meta:
        model = Usuario
        fields = (

            'name',
            'username',
            'email',
            'address',
            'postss',
        )

class AddressSerializerDetail(serializers.HyperlinkedModelSerializer):

    geo = GeoSerializer(read_only=True)



    class Meta:
        model = Address
        fields = (

            'pk',
            'street',
            'suite',
            'city',
            'zipcode',
            'geo',



        )



