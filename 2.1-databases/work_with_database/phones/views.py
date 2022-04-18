from http.client import HTTPResponse

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {
        # 'phones': Phone.objects.all()
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context ={
        # 'phones': Phone,

    }
    return render(request, template, context)

# def show_list(request):
#     phone_objects = Phone.objects.all()
#     phone = [f'{p.id}' for p in phone_objects ]
#     return HTTPResponse(f'{phone}')