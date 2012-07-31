from django.conf.urls.defaults import *

urlpatterns = patterns('reg.views',
    url(r'^login/$', 'do_login'),
    url(r'^logout/$', 'do_logout'),
    url(r'^sign_up/$', 'sign_up'),
)
