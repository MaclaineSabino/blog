"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from postagens import views

urlpatterns = [
    url(r'^users/$',
        views.UsuarioList.as_view(),
        name=views.UsuarioList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UsuarioDetail.as_view(),
        name=views.UsuarioDetail.name),

    url(r'^address/$',
        views.AddressList.as_view(),
        name=views.AddressList.name),

    url(r'^address/(?P<pk>[0-9]+)/$',
        views.AddressDetail.as_view(),
        name=views.AddressDetail.name),
    url(r'^geo/$',
        views.GeoList.as_view(),
        name=views.GeoList.name),
    url(r'^geo/(?P<pk>[0-9]+)/$',
        views.GeoListDetail.as_view(),
        name=views.GeoListDetail.name),

    url(r'^posts/$',
        views.PostList.as_view(),
        name=views.PostList.name),

    url(r'^posts/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(),
        name=views.PostDetail.name),

    url(r'^comments/$',
        views.CommentList.as_view(),
        name=views.CommentList.name),

    url(r'^comments/(?P<pk>[0-9]+)/$',
        views.CommentDetail.as_view(),
        name='comment-detail'),

    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
