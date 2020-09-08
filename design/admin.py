from django.contrib import admin
from .models import Category, Cardtype, Edge, Header, Papermake, Papertype, Quantity, Thicknes, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'company',
        'address',
        'tel',
        'email',
        'category',
        'edge',
        'cardtype',
        'thicknes',
        'paper',
        'make',
        'header',
        'footer',
        'info',
        'price',
        'quantity',
        'logo',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class CardtypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price'
    )


class EdgeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price'
    )


class HeaderAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class PapermakeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price'
    )


class PapertypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price'
    )


class QuantityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ThicknesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cardtype, CardtypeAdmin)
admin.site.register(Edge, EdgeAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Papermake, PapermakeAdmin)
admin.site.register(Papertype, PapertypeAdmin)
admin.site.register(Quantity, QuantityAdmin)
admin.site.register(Thicknes, ThicknesAdmin)
