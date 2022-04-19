from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones': Phone.objects.all(),
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.all()
    for ph in phone_object:
        if ph.slug == slug:
            pk_find = ph.id
    template = 'product.html'
    context ={
        'phone': Phone.objects.get(id=pk_find),
    }
    return render(request, template, context)
