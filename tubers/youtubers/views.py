from ast import keyword
from django.shortcuts import render, get_object_or_404
from .models import Youtuber
from weblink.models import linker

# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_youtubers = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_youtubers = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_youtubers = Youtuber.objects.values_list('category', flat=True).distinct()
    weber = linker.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)  

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)


    data = {
        'tubers': tubers,
        'city_youtubers': city_youtubers,
        'camera_type_youtubers': camera_type_youtubers,
        'category_youtubers': category_youtubers,
        'weber': weber,
    }
    return render(request,'youtubers/youtubers.html',data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    weber = linker.objects.all()

    data = {
        'tuber': tuber,
        'weber' : weber,
    }
    return render(request,'youtubers/youtubers_detail.html', data)


def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)  

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)         
                                   

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search
    }        
    return render(request,'youtubers/search.html', data)