from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    descrition = models.TextField()
    image = models.FileField(upload_to='category/', null=True)

    object = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Dishes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    photo = models.FileField(upload_to='dishes/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    object = models.Manager

    def show_image(self):
        return format_html(f'<img src="/static/media/{self.photo}" width=50 alt="{self.name}">')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dishes'
        verbose_name = 'dishes'
        verbose_name_plural = 'dishes'


class Visitors(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=255)
    otp = models.IntegerField(null=True)
    object = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'visitors'

class Cart(models.Model):
    item = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    dish = models.ForeignKey(to=Dishes, on_delete=models.CASCADE)
    visitor = models.ForeignKey(to=Visitors, on_delete=models.CASCADE)
    object = models.Manager

    def __str__(self):
        return self.item

    class Meta:
        db_table = 'cart'

class Order(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    visitor = models.ForeignKey(to=Visitors, on_delete=models.CASCADE)
    total = models.FloatField()
    object = models.Manager

    def __str__(self):
        return self.id
    class Meta:
        db_table = 'orders'

class OrderDetail(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(to=Dishes, on_delete=models.CASCADE)
    price = models.FloatField()
    total = models.FloatField()
    quantity = models.IntegerField()
    object = models.Manager

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'ordersdetails'