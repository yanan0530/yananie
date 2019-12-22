from django.contrib import admin

# Register your models here.
from .models import GoodsCategroy, GoodsCategroyBrand, Goods ,GoodsImage

admin.site.register(GoodsCategroy)
admin.site.register(GoodsCategroyBrand)
admin.site.register(Goods)
admin.site.register(GoodsImage)
