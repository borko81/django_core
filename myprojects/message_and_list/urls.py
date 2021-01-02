from django.urls import path
from .views import home, next_page, home_view, about_view, ProductList

urlpatterns = [
    path('', home, name='index'),
    path('next_page/', next_page, name='next_page'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('product_list/', ProductList.as_view(), name='product_list'),
]
