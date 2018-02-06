from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(index)?$', views.IndexView.as_view(), name='index'),
    url(r'^posts/$', views.PostsView.as_view(), name='posts'),
    url(r'^article/(?P<aid>[0-9]+)/$', views.ArticleView.as_view(), name='detail'),
    url(r'^(?P<id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^sign-in/$', views.sign_in, name='sign-in'),
    url(r'^sign-up/$', views.sign_up, name='sign-up'),
    url(r'^sign-out/$', views.sign_out, name='sign-out'),
]
