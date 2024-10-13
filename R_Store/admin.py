from django.contrib import admin
from R_Store import models
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'get_discount_price', 'get_full_info')
    search_fields = ('name',)
    list_filter = ('category',)

    def get_discount_price(self, obj):
        return obj.get_discount_price(10)
    get_discount_price.short_description = 'цена со скидкой 10%'

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_full_name')
    search_fields = ('username', 'email')



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at', 'commentary')
    list_filter = ('rating',)
    search_fields = ('user__username', 'product__name')