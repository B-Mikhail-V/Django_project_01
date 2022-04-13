from django.http import HttpResponse
# from recipes.make_content import *
from django.shortcuts import render
from recipes.make_content import make_content, DATA


def create_list(request):
    recipe_name = request.GET.get('recipe', 'empty')
    qty_dishe = request.GET.get('qty', 1)
    context = {
        'recipe': make_content(DATA, recipe_name, qty_dishe),
        'recipe_text': recipe_name,
        'recipe_qty': qty_dishe,

    }
    return render(request, 'calculator/index.html', context)
