from django.contrib import admin
from .models import Product,CarouselImages,Contact,Order,OrderUpdate
# Register your models here.

admin.site.register(Product)
admin.site.register(CarouselImages)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)