from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import status
from .models import Goods, GoodsCategroy
from .serializers import GoodsSerializers, GoodsCategroySerializer


class GoodsListView(APIView):
    '''
    获取所有商品
    '''

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_json = GoodsSerializers(goods, many=True)
        return Response(goods_json.data)

    """
    创建商品
    """

    def post(self, request):
        serializer = GoodsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GoodsList2View(generics.ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers


class GoodsList3View(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    def get_queryset(self):
        return Goods.objects.filter(shop_price__gt=100)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表分类
    """
    queryset = GoodsCategroy.objects.all()
    serializer_class = GoodsCategroySerializer
    # authentication_classes = (TokenAuthentication,)
