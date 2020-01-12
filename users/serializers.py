from rest_framework import serializers
from .models import UserProfile
from rest_framework.validators import UniqueValidator


class MobileSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        # 手机是否存在
        if UserProfile.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")
        # 验证手机号是否合法

        return mobile


class UserRegSersializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="用户已存在")]
                                     )
    password = serializers.CharField(label="密码", write_only=True)
    """
        密码
    """
    def create(self, validated_data):
        user = super(UserRegSersializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = UserProfile
        fields = ("username", "mobile", "password")
