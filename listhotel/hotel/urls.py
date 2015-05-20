from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<hotel_id>[0-9]+)/$', views.detail, name='hotel_id'),
    # ex: /polls/5/results/
    url(r'^(?P<hotel_id>[0-9]+)/galery/$', views.galery, name='hotel_id'),
    # ex: /polls/5/vote/
    url(r'^(?P<hotel_id>[0-9]+)/ranking/$', views.ranking, name='hotel_id'),

]
