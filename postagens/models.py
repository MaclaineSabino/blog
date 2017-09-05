from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Geo(models.Model):
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)


class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    geo = models.ForeignKey(Geo,
                            related_name='geos',
                            on_delete=models.CASCADE)

class Usuario(models.Model):


    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.ForeignKey(Address,
                                related_name='enderecos',
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(Usuario,
                              related_name='postss',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title






class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    post = models.ForeignKey(Post,
                             related_name='comentarios_do_post',
                             on_delete=models.CASCADE,)

    class Meta:
        unique_together = ('post', 'name')
        ordering = ['name',]

    def __str__(self):
        return self.name


    def __unicode__(self):
        return '%s: %s' %(self.name, self.email)

