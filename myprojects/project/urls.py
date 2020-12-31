from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/', include('app01.urls')),
    path('app02/', include('app02.urls')),
    path('app03/', include('app03.urls')),
    path('mandl/', include('message_and_list.urls')),
]
