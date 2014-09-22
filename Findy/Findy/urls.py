from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Findy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'clientApp.views.home', name="home"),
	url(r'^search$', 'clientApp.views.search', name="search"),
    url(r'^indexer/', include('indexer.urls')),
    url(r'^login', 'indexer.views.admin_login', name='login'),
    url(r'^logout', 'indexer.views.admin_logout', name='logout'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
