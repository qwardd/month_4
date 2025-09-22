from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms 
from django.views import generic

class CreateBasket(generic.CreateView):
    model = models.Basket
    form_class = forms.BasketForm
    template_name = 'create_basket.html'
    success_url = '/basket_list/'

class ReadBasketViews(generic.ListView):
    models = models.Basket
    template_name = 'basket_list.html'
    context_object_name = 'basket'
    ordering = ['-id']


class UpdateBasketViews(generic.UpdateView):
    model = models.Basket
    form_class = forms.BasketForm
    template_name = 'update_basket.html'
    success_url = '/basket_list/'
    
    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketViews, self).form_valid(form=form)
    
class DeleteBasketViews(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/basket_list/'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)




