from django.contrib import admin
from beautyapp.models import Category, Product, ProductImage, CartOrder, CartOrderItem, ProductView, wishlist, Address


class ProductImageAdmin(admin. TabularInline):
    model = ProductImage
    
class ProductAdmin(admin. ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['user', 'title', 'product_images', 'price', 'featured', 'product_status' ]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_images']
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date',  'product_status']
    
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'price', 'images', 'item', 'total', 'Qty', ]
    
class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']
    
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status' ]
    
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(Farmer, FarmerAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemAdmin)
admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
    