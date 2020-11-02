from django.contrib import admin

from .models import customerclass, productclass, orderclass,  orderitemclass, shippingaddressclass

admin.site.register(customerclass)
admin.site.register(productclass)
admin.site.register(orderclass)
admin.site.register(orderitemclass)
admin.site.register(shippingaddressclass)
