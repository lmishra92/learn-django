"""testwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path
from restaurants.views import restaurant_createview, \
    RestaurantListView, \
    RestaurantDetailView, \
    RestaurantCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', restaurant_createview, name="home"),
    path('restaurants/', RestaurantListView.as_view(), name="restaurant_page"),
    path('restaurants/create/', RestaurantCreateView.as_view()),
    # re_path('restaurants/(?P<slug>[\w+-])/', RestaurantListView.as_view(), name="search_restaurant_page"),
    re_path('restaurants/(?P<slug>[\w-]+)/', RestaurantDetailView.as_view(), name="search_restaurant_detail_page"),

    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('shop/', include('shop.urls', namespace='shop')),

]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
