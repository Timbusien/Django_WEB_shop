"""
URL configuration for Django1 project.

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
from django.urls import path, include
from django.conf.urls.static import  static
from Django1 import settings
from items.views import home, Shop_Page, ShopDetail, LoginView, LogoutView, RegisterView, ProfileView, add_to_favorite


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('shop', Shop_Page.as_view(), name='shop'),
    path('signup', RegisterView.as_view, name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('accounts/profile', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('shop/<int:pk>', ShopDetail.as_view(), name='shop-detail'),
    path('add_to_favorite/<int:product_id>/', add_to_favorite, name='add_to_favorite'),
    path('accounts/', include('allauth.urls')),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

