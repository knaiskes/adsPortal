from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView

from ads.forms import PostAdForm

from .models import Ad

class IndexView(generic.ListView):
    template_name = 'ads/index.html'
    context_object_name = 'latest_ad_list'

    def get_queryset(self):
        return Ad.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'ads/detail.html'


class PostAdView(FormView):
    #model = Ad
    template_name = 'ads/add.html'
    form_class = PostAdForm
    success_url = '/ads/post-ad'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AboutView(generic.ListView):
    model = Ad
    template_name = 'ads/about.html'
