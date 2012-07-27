from django.conf.urls.defaults import *

urlpatterns = patterns('uTriga.views',
    url(r'^$', 'home'),
    url(r'^post/$','post_advert'),
    url(r'^post/all/$','see_posts'),
    url(r'^services/$','services'),
    url(r'^projects/$','projects'),
    url(r'^about/$','about_us'),
    url(r'^contact/$','contact_us'),
    url(r'^boot/$','boot_test'),
    ## add your url here
)
