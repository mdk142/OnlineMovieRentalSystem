from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.index', name='index'),
)
