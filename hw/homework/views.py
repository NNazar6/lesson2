from django.http import HttpResponse
from django.urls import path


def index(request):
    host = request.META['HTTP_HOST']
    user_data = request.META['HTTP_USER_AGENT']
    ip_user = request.META['REMOTE_ADDR']
    return HttpResponse(f'{host}, {user_data}, {ip_user}')


def error(request):
    return HttpResponse(f'К сожалению произошла ошибка', status=404, reason='List not found')


def user(request, name='Sir', age=0, login=11111, folder='default', numf=1):
    return HttpResponse(
        f'<h1>Ваше имя, Сэр: {name} Ваш возраст составляет: {age}, мистер молодой Сэр. Ваш логин, Сэр - {login}. Папка с вашими проектами: {folder}, проект №{numf}')
