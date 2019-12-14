from django.urls import path
from . import views


app_name = "excelcms"
urlpatterns = [
    path('userinfo', views.index),
    path('login', views.loginCms),
    path('fileExcel', views.fileExcel),
    path('splicingCell',views.splicingCell)
]
