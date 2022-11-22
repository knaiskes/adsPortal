#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Ad

def index(request):
    latest_ad_list = Ad.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.title for a in latest_ad_list])
    context = { 'latest_ad_list': latest_ad_list }
    return render(request, 'ads/index.html', context)

def detail(request, ad_id):
    return HttpResponse("This is the details page for: %s" % ad_id)
