from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from tours.models import Tourist, Tour

def tourist_detail(request, id):
    if request.method == 'GET':
        tourist_id = get_object_or_404(Tourist, id=id)
        context = {
            'tourist_id': tourist_id
        }
    return render(request, template_name='tourist_detail.html', context=context)
    


def tour_list(request):
    if request.method == 'GET':
        tour_list = Tour.objects.all().order_by('-id')
        context = {
            'tour_list': tour_list,
        }
    return render(request, template_name='tour_list.html', context=context)
