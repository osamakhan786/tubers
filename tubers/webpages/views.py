from django.shortcuts import render
from .models import Abouter, Slider, Team
from youtubers.models import Youtuber
from weblink.models import linker

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    weber = linker.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_date')

    data = {
        'sliders': sliders,
        'teams': teams,
        'weber': weber,
        'featured_youtubers': featured_youtubers,
        'all_tubers': all_tubers
    }
    return render(request, 'webpages/home.html',data)


def about(request):
    teams = Team.objects.all()
    abouter = Abouter.objects.all()
    weber = linker.objects.all()

    data = {
        'teams': teams,
        'abouter': abouter,
        'weber' : weber,
    }

    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    weber = linker.objects.all()

    data = {
        'weber': weber,
    }

    return render(request, 'webpages/contact.html', data)