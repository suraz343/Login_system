"""
URL configuration for login_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path as url
from django.urls import path, include
from myapp import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    
    ##### user related path##########################
    path('', include('myapp.urls')),
    path('login', user_view.Login, name ='login'),
    path('logout', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register', user_view.register, name ='register'),

]