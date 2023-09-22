from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib import admin
#Django admin header customization
admin.site.site_header ="Welcome to admin Dashboard"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Admin DashBoard"

urlpatterns = [
    path('', views.index, name ='index'),
]