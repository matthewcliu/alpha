from django.conf.urls.defaults import patterns, url

from myapp1 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)