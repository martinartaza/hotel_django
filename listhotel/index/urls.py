from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /index/
    url(r'^$', views.index, name='index'),
]