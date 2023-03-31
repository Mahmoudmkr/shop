from django.urls import path
from . import views

urlpatterns=[
    path('', views.ShopListView.as_view(),name='shopp_list'),
    path('shopp/create',views.ShopCreateView.as_view(),name='create'),
    path('shopp/edit/<int:pk>',views.ShopUpdateView.as_view(),name='update'),
    path('shopp/delete/<int:pk>',views.ShopDeleteView.as_view(),name='delete'),
    path('task/create',views.TaskCreateView.as_view(),name='task_create'),
    path('task/edit/<int:pk>',views.TaskUpdateView.as_view(),name='task_update'),
    path('task/delete/<int:pk>',views.TaskDeleteView.as_view(),name='task_delete'),

]