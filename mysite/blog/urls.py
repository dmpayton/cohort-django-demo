from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.PostList.as_view(),
        name='post-list'),

    url(r'^(?P<pk>[0-9])/$',
        views.PostDetail.as_view(),
        name='post-detail'),

    url(r'^(?P<pk>[0-9])/comment/$',
        views.CreateComment.as_view(),
        name='create-comment'),
]
