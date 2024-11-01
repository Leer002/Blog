from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Product, Comment
from .forms import ProductForm, CommentForm

 
class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        form = ProductForm()
        return render(request, "gallery/index.html", {"products":products, "form":form, "user":request.user})
    
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
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
        return render(request, "gallery/edit.html", {"form":form, "product": product})
    
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
    

class UserProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        products = Product.objects.filter(user=user)
        form = ProductForm()
        return render(request, "gallery/profile.html", {"products":products, "form":form, "user":user})
    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
            user=user,
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image'])
            product.save()
        products = Product.objects.filter(user=user)
        return render(request, "gallery/profile.html", {"products":products, "form":form})