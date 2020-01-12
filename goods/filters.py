from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品过滤类
    """
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = filters.NumberFilter(method='top_category_filter')

    def top_category_filter(selfs, queryset, name, value):
        queryset = queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))
        return queryset

    class Meta:
        model = Goods
        fields = ['min_price', 'max_price', 'name']
