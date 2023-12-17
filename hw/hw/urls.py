from django.contrib import admin
from django.urls import path, re_path
from homework import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/(?P<login>\d+)/(?P<folder>\d+)/(?P<numf>\d+)', views.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/(?P<login>\d+)/(?P<folder>\w+)', views.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/(?P<login>\d+)', views.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user),
    re_path(r'^user/(?P<name>\D+)', views.user),
    re_path(r'^user', views.user),
    re_path(r'^error', views.error),
    re_path(r'^index', views.index),
]
