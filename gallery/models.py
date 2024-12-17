from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="products/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()


    def short_description(self):
        words = self.description.split()
        if len(words) > 50:
            return ' '.join(words[:30]) + '...'
        else:
            return self.description
   

class Comment(models.Model):
    product = models.ForeignKey(Product, verbose_name="comment", related_name="%(class)s", on_delete=models.CASCADE)
    text = models.TextField()
    user_name = models.CharField(max_length=40, default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_name}: {self.text}"
