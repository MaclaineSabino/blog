from django.db import models

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
                            on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.ForeignKey(Address,
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User,
                             related_name='posts',
                             on_delete=models.CASCADE,)


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    post = models.ForeignKey(Post,
                             related_name='comentarios_do_post',
                             on_delete=models.CASCADE,)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

