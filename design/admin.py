from django.contrib import admin
from .models import Category, Cardtype, Edge, Header, Papermake, Papertype, Quantity, Thicknes, Product

# Register your models here.


admin.site.register(Category)
admin.site.register(Cardtype)
admin.site.register(Edge)
admin.site.register(Header)
admin.site.register(Papermake)
admin.site.register(Papertype)
admin.site.register(Quantity)
admin.site.register(Thicknes)
admin.site.register(Product)
