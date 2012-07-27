from django.conf.urls import patterns, include, url
from django.conf import settings
from uTriga.api import UserResource,EventResource,CategoryResource 

event_resource = EventResource()
user_resource = UserResource()
category_resource = CategoryResource()


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls)),
url(r'^utriga/', include('uTriga.urls')),
url(r'^utriga/reg/', include('reg.urls')),
url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root' : settings.STATIC_ROOT,}),
url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root' : settings.MEDIA_ROOT,}),
(r'^event/', include(event_resource.urls)),
(r'^user/', include(user_resource.urls)),
(r'^category/', include(category_resource.urls)),
                                             
)
