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
from django.conf.urls import url,include
from django.contrib import admin
from postagens import views

urlpatterns = [
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),

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
        name=views.CommentDetail.name),

    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
