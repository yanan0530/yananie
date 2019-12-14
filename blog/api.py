from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Topmenu, Banner

from django.contrib.auth.models import User
from django.contrib.auth import login as loginL, authenticate


class TopMenuList(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Topmenu
        fields = '__all__'


class BannerList(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Banner
        fields = '__all__'


@api_view(['GET'])
def listMenu(resquest):
    topmenu = Topmenu.objects.all()
    topmenuData = TopMenuList(topmenu, many=True)

    return Response({'topmenu': topmenuData.data})


@api_view(['GET'])
def index(request):
    banner = Banner.objects.all()
    bannerList = BannerList(banner, many=True)
    userid = request.user
    print(userid.id)
    return Response({'banner': bannerList.data})


@api_view(['POST'])
def login(request):

    userid=request.user
    print(userid.id)

    if userid != 'AnonymousUser':
        loginType='ok'


    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user != None:
            loginL(request, user)
            return Response({"loginType": 'ok'})


    return Response({"loginType": loginType})

