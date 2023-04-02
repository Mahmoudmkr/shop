from django.urls import reverse_lazy, reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
# Create your views here.


class ShopListView(ListView):
    model = models.Shop
    template_name = 'shopp/list.html'
    paginate_by = 3
    def get_queryset(self):
        query_set=super().get_queryset()
        where={}
        q=self.request.GET.get('q',None)
        if q:
            where['title__icontains']=q
        return query_set.filter(**where)

class ShopCreateView(CreateView):
    model=models.Shop
    form_class = forms.ShopCreateForm
    template_name = 'shopp/create.html'
    success_url = reverse_lazy('shopp_list')

class ShopUpdateView(UpdateView):
    model=models.Shop
    form_class = forms.ShopUpdateForm
    template_name = 'shopp/update.html'
    success_url = reverse_lazy('shopp_list')

   # def get_success_url(self):
    #    return reverse ('update',args=[self.object.id])

class ShopDeleteView(DeleteView):
    model=models.Shop
    template_name = 'shopp/delete.html'
    success_url = reverse_lazy('shopp_list')


class TaskCreateView(CreateView):
    model=models.Task
    fields=['description','shop']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('update', args=[self.object.shop.id])

class TaskUpdateView(UpdateView):
    model=models.Task
    fields=['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('update', args=[self.object.shop.id])

class TaskDeleteView(DeleteView):
    model=models.Task

    def get_success_url(self):
        return reverse('update', args=[self.object.shop.id])

