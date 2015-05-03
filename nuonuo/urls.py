from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import xadmin

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nuonuo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'admin/', include(xadmin.site.urls)),
    url(r'get_location/$', "misc.views.get_location", name="get-location"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
