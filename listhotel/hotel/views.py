from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Hotel, Galery, Ranking


def index(request):
    list_hotel = hotel.objects.order_by('-pub_date')[:5]
    template = loader.get_template('hotel/index.html')
    context = RequestContext(request, {
        'list_hotel': list_hotel,
    })
    return HttpResponse(template.render(context))


def detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel/detail.html', {'hotel': hotel})


def galery(request, hotel_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % hotel_id)


def ranking(request, hotel_id):
    return HttpResponse("You're voting on question %s." % hotel_id)
