from django.shortcuts import render
from postagens.models import *
from postagens.serializers import *
import json
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from postagens.permissions import *
from rest_framework.decorators import api_view
from django.contrib.auth.models import User






class GeoList(generics.ListCreateAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    name='geo-list'

class GeoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    name='geo-list-detail'

class UsuarioList(generics.ListAPIView):
   queryset = Usuario.objects.all()
   serializer_class = UserSerializer
   name = 'user-list'


   permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )




class UsuarioDetail(generics.ListAPIView):
   queryset = Usuario.objects.all()
   serializer_class = UserSerializerDetail
   name='user-detail'
   permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )
class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    name='address-list'

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializerDetail
    name='address-detail'
    permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name='post-list'

    permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )

    def perform_create(self, serializer):
        usuario = Usuario.objects.get(user=self.request.user)
        serializer.save(owner=usuario)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerComentarios
    name='post-detail'

    permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-list'
    permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly,

   )



class CommentDetail(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-detail'
    permission_classes = (
       permissions.IsAuthenticatedOrReadOnly,
       comentarios,

   )





class ApiRoot(generics.GenericAPIView):
  name='api-root'

  def get(self,request,*args,**kwargs):

      return Response({
          'usuarios':reverse(UsuarioList.name,request=request),
          'posts':reverse(PostList.name,request=request),
          'comentarios':reverse(CommentList.name,request=request)




      })
















#GRANDE CONTRIBUIÇÃO DO NOSSO COLEGA GILDÁSIO, OS CRÉDITOS DESSE SCRIPT SÃO DELE
'''SCRIPT MODIFICADO POR MACLAINE, PARA AO CADASTRAR OS USUÁRIOS, SEJA TAMBÉM CRIADO OS 10 LOGINS
COM USERNAME,EMAIL E SENHA. A SENHA FOI CRIADA COMO NOME USERNAME + 123, NA CRIAÇÃO DOS POSTS O OWNER JÁ RECEBE
OS IDS DOS USUÁRIOS QUE ESTÃO CADASTRADOS NO USERS DOS DJANGOS, SENDO QUE SÃO OS MESMOS QUE CRIARAM OS POSTS
'''
def import_data():
    dump_data = open('db.json', 'r')
    as_json = json.load(dump_data)
    for user in as_json['users']:
        usuar =User.objects.create_user(user['username'],user['email'],user['username']+'123')
        usuar.save()
        geo = Geo.objects.create(lat=user['address']['geo']['lat'],
                                 lng=user['address']['geo']['lng'])
        address = Address.objects.create(street=user['address']['street'],
                                         suite=user['address']['suite'],
                                         city=user['address']['city'],
                                         zipcode=user['address']['zipcode'],
                                         geo=geo)
        userescr = Usuario(id=user['id'],
                            user=usuar,
                            name=user['name'],
                            username=user['username'],
                            email=user['email'],
                            address=address)
        userescr.save()


    for post in as_json['posts']:
        usuario = Usuario.objects.get(id=post['userId'])


        Post.objects.create(id=post['id'],
                            owner = usuario,
                            title=post['title'],
                            body=post['body'],

                            )


    for comment in as_json['comments']:
        post = Post.objects.get(id=comment['postId'])
        Comment.objects.create(id=comment['id'],
                               name=comment['name'],
                               email=comment['email'],
                               body=comment['body'],
                               post=post)




