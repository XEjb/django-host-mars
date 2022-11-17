from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "Инфа", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Фидбэк", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'}
        ]


def index(request):
    posts = Yukiko.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'yukiko/index.html', context=context)


def about(request):
    return render(request, 'yukiko/about.html', {'menu': menu, 'title': 'Инфа'})


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse("Фидбэк")


def login(request):
    return HttpResponse('Вход')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(requset, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
