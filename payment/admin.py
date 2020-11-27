from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_purchase',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email',  'street_address1', 'street_address2',
              'town_or_city', 'county', 'postcode', 'country',
              'phone_number', 'delivery_cost', 'order_total',
              'grand_total', 'original_purchase', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
