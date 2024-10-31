from django.contrib import admin

from .models import Product, Comment

class CommentAdmin(admin.TabularInline):
    model = Comment
    fields = ["user_name", "text"]
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [CommentAdmin]