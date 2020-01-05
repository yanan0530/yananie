from django.urls import path, include
from goods.views import GoodsListView, GoodsList2View, GoodsList3View, CategoryViewset

from rest_framework.routers import DefaultRouter

app_name = "goods"

goods_list = GoodsList3View.as_view({
    'get': "list",
})

router = DefaultRouter()

router.register(r'list4', GoodsList3View)
router.register(r'categorys', CategoryViewset)
urlpatterns = [
    path('list', GoodsListView.as_view(), name="goods_list"),
    path('lis2t', GoodsList2View.as_view(), name="goods_list2"),
    path('list3', goods_list),
    path("", include(router.urls))
]
