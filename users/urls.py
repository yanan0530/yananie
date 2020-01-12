from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import UserViewset

app_name = "users"
router = DefaultRouter()
router.register(r'users', UserViewset,basename="user")
urlpatterns = [
    url(r'^', include(router.urls)),
]
