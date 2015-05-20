from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import RequestContext, loader

from hotel.models import Hotel


def index(request):
    Hotel_list = Hotel.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index/index.html')
    context = RequestContext(request, {
        'list_hotel': Hotel_list,
    })
    return HttpResponse(template.render(context))
