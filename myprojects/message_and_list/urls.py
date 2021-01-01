from django.urls import path
from .views import home, next_page

urlpatterns = [
    path('', home, name='index'),
    path('next_page/', next_page, name='next_page'),
]
