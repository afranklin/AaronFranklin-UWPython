from django.conf.urls.defaults import *

urlpatterns = patterns('recipefind.views',
    (r'^$', 'index'),
    (r'^(?P<recipe_id>\d+)/$', 'detail'),
    (r'^(?P<ingredient>\w+)/$', 'ingredient'),
)
