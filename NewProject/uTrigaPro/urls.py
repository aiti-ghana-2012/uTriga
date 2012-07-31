from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from uTriga.api import UserResource,EventResource,CategoryResource 
from django.contrib.auth.views import password_reset

v1_api = Api(api_name='utriga')
v1_api.register(UserResource())
v1_api.register(EventResource())
v1_api.register(CategoryResource())


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
<<<<<<< HEAD
(r'^event/', include(event_resource.urls)),
(r'^user/', include(user_resource.urls)),
(r'^category/', include(category_resource.urls)),
 (r'^reset/$', 'uTriga.views.reset_password'),
                             
=======
(r'^api/', include(v1_api.urls)),
                                             
>>>>>>> 95d99323dcef77f986e14798972f70048d0ce44a
)
