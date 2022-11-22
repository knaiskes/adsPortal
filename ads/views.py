from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Ad

def index(request):
    latest_ad_list = Ad.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.title for a in latest_ad_list])
    context = { 'latest_ad_list': latest_ad_list }
    return render(request, 'ads/index.html', context)

def detail(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    return render(request, 'ads/detail.html', {'ad': ad})
