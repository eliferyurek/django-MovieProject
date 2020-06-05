from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(AddressCustomer)
admin.site.register(Order)
admin.site.register(MovieOrder)
admin.site.register(City)
admin.site.register(Store)
