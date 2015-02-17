from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'argo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # make it so that it responds to blank url extension
    url(r'^$', include('jason.urls')),
    # url(r'^jason/', include('jason.urls')), 
)
