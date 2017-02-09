from django.conf.urls import url

from .views import PostDetail, PostList

urlpatterns = [
    url(r'^$', PostList.as_view()),
    url(r'^(?P<pk>[0-9])/$', PostDetail.as_view()),
]
