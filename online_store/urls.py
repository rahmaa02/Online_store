"""
URL configuration for online_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from R_Store import views



from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.conf.urls.static import  static


router = DefaultRouter()

router.register('users', views.UserAPI, basename='users')
router.register('orders', views.OrderAPI, basename='orders')
router.register('categories', views.CategoryAPI, basename='categories')
router.register('products', views.ProductAPI, basename='products')
router.register('reviews', views.ReviewAPI, basename='reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name = 'schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),

    path('', include('R_Store.urls')),


] + router.urls
