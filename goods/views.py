from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializers


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
