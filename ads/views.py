#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Ad

def index(request):
    latest_ad_list = Ad.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.title for a in latest_ad_list])
    templete = loader.get_template('ads/index.html')
    context = {
        'latest_ad_list': latest_ad_list
    }
    return HttpResponse(templete.render(context, request))

def detail(request, ad_id):
    return HttpResponse("This is the details page for: %s" % ad_id)
