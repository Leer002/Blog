from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .models import Product, Comment
from .forms import ProductForm, CommentForm

 
class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        form = ProductForm()
        return render(request, "gallery/index.html", {"products":products, "form":form})
    
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        products = Product.objects.all()
        return render(request, "gallery/index.html", {"form":form, "products":products})
    
class ProductDetailView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            comments = Comment.objects.all()
            form = CommentForm()
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        return render(request, "gallery/index2.html", {"product":product, "form":form, "comments":comments})
    
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            messages.success(request, "Comment added successfully!")
        return redirect("detail", pk=pk)


class EditView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        form = ProductForm()
        return render(request, "gallery/edit.html", {"form":form})
    
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("list")
        return render(request, "gallery/edit.html", {"form":form})

class DeleteView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        return render(request, "gallery/delete.html", {"product":product})
    
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        product.delete()
        return redirect("list")
    
