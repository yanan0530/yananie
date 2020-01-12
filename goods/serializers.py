from rest_framework import serializers

from .models import Goods, GoodsCategroy, GoodsImage


# class GoodsSerializers(serializers.Serializer):
#     # name = serializers.CharField(required=True, max_length=100)
#     # click_num = serializers.IntegerField(default=0)
#     # goods_front_image = serializers.ImageField()
#     #
#     # def create(self, validated_data):
#     #     return Goods.objects.create(**validated_data)
#
#     class Meta:
#         model = Goods
#         fields = "__all__"


class CategroySerializer3(serializers.ModelSerializer):
    """
    商品类别序列化
    """

    class Meta:
        model = GoodsCategroy
        fields = "__all__"


class CategroySerializer2(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategroySerializer3(many=True)

    class Meta:
        model = GoodsCategroy
        fields = "__all__"


class GoodsCategroySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategroySerializer2(many=True)

    class Meta:
        model = GoodsCategroy
        fields = "__all__"


class GoodsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ('image',)

class GoodsSerializers(serializers.ModelSerializer):
    category = GoodsCategroySerializer()
    images=GoodsImageSerializers(many=True)
    class Meta:
        model = Goods
        # fields=('name','category','goods_sn','click_num')
        fields = "__all__"

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)
