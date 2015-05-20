from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('index.urls')),
    url(r'^hotel/', include('hotel.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
