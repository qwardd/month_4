from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from tours.models import Tourist, Tour
from django.views import generic

class ToursDetailView(generic.DetailView):
    template_name = 'tourist_detail.html'
    context_object_name = 'tourist_id'

    def get_object(self, *args, **kwargs):
        tourist_id = self.kwargs.get('id')
        return get_object_or_404(Tour, id=tourist_id)



class ToursListViews(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tour_list'
    ordering = ['-id']

    def get_queryset(self):
        return Tour.objects.all()


