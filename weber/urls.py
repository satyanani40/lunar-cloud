from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from weber import settings
admin.autodiscover()

import api.service
import api.matchme
import api.user

# urllist = ('',
#     # Examples:
#     # url(r'^$', 'weber.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )

public_urls = lambda api_module: getattr(api_module, 'urlpatterns', patterns('',))

public_patterns = patterns('')
public_patterns += public_urls(api.service)
public_patterns += public_urls(api.user)
public_patterns += public_urls(api.matchme)
urlpatterns = public_patterns

