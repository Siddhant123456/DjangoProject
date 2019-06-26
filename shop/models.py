from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 30)
    product_desc = models.CharField(max_length = 300)
    price = models.IntegerField(default = 0)
    img = models.ImageField(upload_to = 'shop/images' , default = "")
    category = models.CharField(max_length = 50 , default = "")
    subCategory = models.CharField(max_length = 50 , default = "")
    product_publish = models.DateField()

    def __str__(self):
        return self.product_name
class CarouselImages(models.Model):
    image = models.ImageField(upload_to= 'shop/carousel/images',default = "")


class Contact(models.Model):
    msg_id = models.AutoField(primary_key = 1)
    name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 300)
    email = models.CharField(max_length = 50, default = 0)
   

    def __str__(self):
        return self.name

class Order(models.Model):
    item_json = models.CharField(max_length = 100)
    order_id = models.AutoField(primary_key = True)
    amount = models.IntegerField(default = "0")
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    number = models.IntegerField()
    
    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    order_id = models.IntegerField()
    update_id = models.AutoField(primary_key = True)
    order_desc = models.CharField(max_length = 5000)
    update_time = models.TimeField(auto_now_add = True)
    update_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.order_desc[0:15] + "...."
