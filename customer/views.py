from django.shortcuts import render
from django.views.generic import  ListView, CreateView
from . import models
# Create your views here.


class ShopListView(ListView):
    model = models.Shop
    template_name = 'shop/shopp_list'
