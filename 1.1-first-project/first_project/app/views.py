from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().time()
    time_format = "%H:%M:%S"
    msg = f'Текущее время: {current_time:{time_format}}'
    return HttpResponse(msg)


def workdir_view(request):
    file_list = listdir(path='.')
    msg = f'Список файлов: {file_list}'
    return HttpResponse(msg)
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
