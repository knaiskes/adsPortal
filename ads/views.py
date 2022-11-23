from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Ad

class IndexView(generic.ListView):
    template_name = 'ads/index.html'
    context_object_name = 'latest_ad_list'

    def get_queryset(self):
        return Ad.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'ads/detail.html'
