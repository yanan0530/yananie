from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile

from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .serializers import MobileSerializer, UserRegSersializer
from rest_framework.response import Response
from rest_framework import status
# 生成jwt
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# class CreatUserViewset(CreateModelMixin, viewsets.GenericViewSet):
#     serializer_class = MobileSerializer
#
#     def create(self, request: Request, *args: Any, **kwargs: Any):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSersializer
    queryset = UserProfile.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
