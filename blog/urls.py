from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^montreal', views.montreal, name='montreal'),
    url(r'^toronto', views.toronto, name='toronto'),
    url(r'^about', views.about, name='about'),
    url(r'^blog', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^contact/$', views.contact, name='contact'),
]
