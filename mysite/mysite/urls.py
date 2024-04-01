from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^a1/', include('a1.urls')),
    url(r'^', include('webapp.urls')),
    url(r'^blog/', include('blog.urls')),
]
