from django.db import models
from account_module.models import User
from product_module.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    is_paid = models.BooleanField(verbose_name='finished / not finished')
    payment_date = models.DateField(null=True, blank=True, verbose_name='pay date')

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Users Basket'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='Final price')
    count = models.IntegerField(verbose_name='count')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'Basket Details'
        verbose_name_plural = 'Basket Details list'
