from django.urls import path
from . import views

urlpatterns=[
    path('', views.ShopListView.as_view,name='shopp_list')

]