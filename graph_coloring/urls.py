from django.conf.urls import patterns, include, url
from django.contrib import admin
from graph.views import graph

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph_coloring.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', graph),
)
