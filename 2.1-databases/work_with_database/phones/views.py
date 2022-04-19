from django.shortcuts import render, redirect

from phones.models import Phone
from phones.sort_dict import sort_dict


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get('sort', 'name')
    template = 'catalog.html'
    context = {
        'phones': Phone.objects.order_by(sort_dict[sort_type]),
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
