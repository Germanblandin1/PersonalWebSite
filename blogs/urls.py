from django.conf.urls import url
from . import views

app_name = 'blogs'


urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^blog/(?P<pk>[0-9]+)$', views.blog_detail_view, name='blog_detail'),
	url(r'^blog-home-1.html$', views.blogs_view, name='blogs_views'),
	url(r'^new_blog.html$', views.new_blog_view, name='new_blog'),
	url(r'[A-Za-z]+', views.manage_views, name='manage'),
	
]
