from django.shortcuts import render
from postagens.models import *
from postagens.serializers import *
import json
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class GeoList(generics.ListCreateAPIView):
    queryset = Geo.objects.all()
    serializer_class = GeoSerializer
    name='geo-list'

class UserList(generics.ListCreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   name='user-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name='post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerComentarios
    name='post-detail'

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name='comment-detail'

class ApiRoot(generics.GenericAPIView):
  name='api-root'

  def get(self,request,*args,**kwargs):

      return Response({
          'users':reverse(UserList.name,request=request),
          'posts':reverse(PostList.name,request=request)



      })








#GRANDE CONTRIBUIÇÃO DO NOSSO COLEGA GILDÁSIO, OS CRÉDITOS DESSE SCRIPT SÃO DELE
def import_data():
    dump_data = open('db.json', 'r')
    as_json = json.load(dump_data)
    for user in as_json['users']:
        geo = Geo.objects.create(lat=user['address']['geo']['lat'],
                                 lng=user['address']['geo']['lng'])
        address = Address.objects.create(street=user['address']['street'],
                                         suite=user['address']['suite'],
                                         city=user['address']['city'],
                                         zipcode=user['address']['zipcode'],
                                         geo=geo)
        User.objects.create(id=user['id'],
                            name=user['name'],
                            username=user['username'],
                            email=user['email'],
                            address=address)

    for post in as_json['posts']:
        user = User.objects.get(id=post['userId'])
        Post.objects.create(id=post['id'],
                            title=post['title'],
                            body=post['body'],
                            user=user)

    for comment in as_json['comments']:
        post = Post.objects.get(id=comment['postId'])
        Comment.objects.create(id=comment['id'],
                               name=comment['name'],
                               email=comment['email'],
                               body=comment['body'],
                               post=post)




