from django.urls import path

from .views import (ProductListView, ProductDetailView, EditView, DeleteView)

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('detail/<int:pk>/edit/', EditView.as_view(), name="edit"),
    path('detail/<int:pk>/delete/', DeleteView.as_view(), name="delete")
]