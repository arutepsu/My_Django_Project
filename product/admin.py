from django.contrib import admin

from product.models import *


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'rate', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']
    list_filter = ['rate', 'created_at']
    ordering = ['created_at']


admin.site.register(Category)
admin.site.register(Review)
