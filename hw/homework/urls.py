from django.urls import path, re_path
from .views import index, error, user


urlpatterns = [
    re_path(r'^', index, name='index'),
]