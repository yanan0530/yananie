from django.urls import path
from . import api

app_name = "blog"
urlpatterns = [
    path('menu/list', api.listMenu),
    path('index/', api.index),
    path("login", api.login)
]
