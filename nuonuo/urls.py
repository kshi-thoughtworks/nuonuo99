from django.conf.urls import patterns, include, url

import xadmin

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nuonuo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'admin/', include(xadmin.site.urls)),
)
