from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product


from django_filters.views import FilterView


from rest_framework import viewsets

from R_Store.models import Product, User, Order, Category, Review
from R_Store import filters
from R_Store import serializers


# Create your views here.

class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.User

class OrderAPI(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializers.Order

class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.Category

class ProductAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.Product

class ReviewAPI(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.Review

class ProductListView(FilterView):
    model = Product
    template_name = 'R_Store/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    filterset_class = filters.ProductFilter

class ProductDetailView(DetailView):
    model = Product
    template_name = 'R_Store/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'R_Store/product_form.html'
    fields = ['name', 'price', 'description', 'stock', 'category', 'image']
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'R_Store/product_form.html'
    fields = ['name', 'price', 'description', 'stock', 'category', 'image']
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'R_Store/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')