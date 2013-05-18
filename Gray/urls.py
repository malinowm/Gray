from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Gray.views.home', name='home'),
    # url(r'^Gray/', include('Gray.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/$', 'blog.views.bloglist'),
    url(r'^blog/(?P<postNo>\d+)/$', 'blog.views.singleblog'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^Xmas/$', 'blog.views.xmas'),
)
