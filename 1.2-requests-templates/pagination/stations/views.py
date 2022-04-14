from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from stations.create_list import create_list


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = request.GET.get('page', 1)
    paginator = Paginator(create_list('data-398-2018-08-30.csv'), 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
