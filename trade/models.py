from datetime import datetime

from django.db import models

from users.models import UserProfile
from goods.models import Goods


# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return "%s(%d)".format(self.goods.name, self.nums)
        return f"{self.goods.name}({self.nums})"


class OrderInfo(models.Model):
    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("cancel", "待支付"),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    order_sn = models.CharField(max_length=30, unique=True, verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="支付编号")
    pay_status = models.CharField(choices=ORDER_STATUS, max_length=10, verbose_name="订单状态")
    post_scipt = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    # pay_type = models.CharField(choices=PAY_TYPE, verbose_name="支付类型", max_length="10")
    address = models.CharField(max_length=100, default='', verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default='', verbose_name="签收人")
    singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo, verbose_name="订单信息", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
