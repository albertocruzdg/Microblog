from django.conf.urls import patterns,url
from posts import views

urlpatterns=patterns('',
	url(r'^$',views.index, name='index'),
	url(r'^post/$',views.post, name='post'),
	url(r'^(?P<post_id>\d+)/$',views.detail, name='detail'),
	url(r'^(?P<post_id>\d+)/comment/$',views.comment, name='comment'),
)