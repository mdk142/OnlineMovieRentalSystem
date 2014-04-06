from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    #url(r'^$', views.search, name='search')
    url(r'^search/', views.search, name='search'),
    url(r'^radha/$', views.radha, name='radha'),
    url(r'^submit/$', views.submit, name='submit'),
    #url(r'^radha/submit/(?P<searchtext>\w+)', views.submit, name='submit'),
    #url(r'^submit/(?P<searchtext>\w+)', views.submit, name='submit'),
    #url(r'^radha/submit/(?P<searchtext>\w+)', views.submit, name='submit'),
    #url(r'^submit/(?P<searchtext>\d+)', views.submit, name='submit'),
    #url(r'^submit/(?P<searchtext>\w{0,50})', views.submit, name='submit'),
    #url(r'^(?P<searchtext>\w+)', views.submit, name='submit'),
)
