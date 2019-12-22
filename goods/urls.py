from django.urls import path
from goods.views import GoodsListView
app_name = "goods"
urlpatterns = [
    path('list',GoodsListView.as_view(),name="goods_list" ),
]
