from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, generics, viewsets, mixins
from .models import Goods, GoodsCategroy
from .serializers import GoodsSerializers, GoodsCategroySerializer
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend


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


class GoodsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    商品列表页，分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief')
    ordering_fields = ['shop_price', 'add_time']


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表分类
    """
    # queryset = GoodsCategroy.objects.all()
    queryset = GoodsCategroy.objects.filter(category_type=1)
    serializer_class = GoodsCategroySerializer
    # authentication_classes = (TokenAuthentication,)
