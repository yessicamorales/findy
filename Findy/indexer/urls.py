from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'indexer.views.indexer_home', name='indexer_home'),
	url(r'^/delete/(?P<id>\d+)/$', 'indexer.views.delete_page', name='delete_page'),
)