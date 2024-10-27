from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from .models import Product
from .forms import ProductForm

 
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
        except Product.DoesNotExist:
            messages.error(request, "Not found")
        return render(request, "gallery/index2.html", {"product":product})

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
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
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