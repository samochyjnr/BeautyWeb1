from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe



STATUS_CHOICE = (
    ('process', "Processing"),
    ('shipped', "Shipped"),
    ('delivered', "Delivered"),
)


STATUS = (
    ('draft', "Processing"),
    ('disabled', "Shipped"),
    ('rejected', "Rejected"),
     ('review', "In Review"),
    ('published', "Published"),
    
    
)

RATING = (
    ( 1, "⭐"),
    ( 2, "⭐⭐"),
    ( 3, "⭐⭐⭐"),
    ( 4, "⭐⭐⭐⭐"),
    ( 5, "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', default='category.jpg')
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def category_images(self):
        return mark_safe('<img src="%s" width="50" height="50 />' %(self.image.url))
    
    def __str__(self):
        return self.title
    
  
class Product(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, default='product.jpg')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default='400')
    old_price = models.DecimalField(max_digits=400, decimal_places=2, default='600')
    specification = models.TextField(null=True, blank=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default='In Review')
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    review = models.TextField()
    
    
    class Meta:
        verbose_name_plural = "Products"
        
    def product_images(self):
        return mark_safe('<img src="%s" width = "50" height= "50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
class ProductImage(models.Model):
    images = models.ImageField(upload_to='product_images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Images"
        
        
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2.0 )
    paid_status = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='Processing')
    
    class Meta:
        verbose_name_plural = "Cart Order"
        
class CartOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    #invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField (max_length=200)
    images = models.CharField (max_length=200)
    Qty = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=800, decimal_places=2, default='200')
    total = models.DecimalField(max_digits=700, decimal_places=2, default='200')
    
    class Meta:
        verbose_name_plural = "Cart Order Items"
        
        
    def Order_Img(self):
        return mark_safe ('<img src="/media/%s" width = "50" height="50">' %(self.image))
    
class ProductView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Product Reviews"
        
        
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
    
class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Wishlists"
        
        
    def __str__(self):
        return self.product.title
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Address"
    
    
    
    
    
