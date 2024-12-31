"""
URL configuration for ecom project.

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
from django.contrib import admin
from django.urls import path
from  login.views import *
from main.views import *
from django.conf.urls.static import static
from django.conf import settings
from cart.views import *

urlpatterns = [
    path('',register,name="register" ),
    path('register/', register, name='register'),
    path('login_page/', login_page, name='login_page'),
    path("after_login/",after_login,name="after_login"),
    path('admin/', admin.site.urls),
    path ("adding_item/",adding_item,name="adding_item"),
    path("buy_product_list/",buy_product_list,name="buy_product_list"),
    path("delete_item/<int:id>/", delete_item, name="delete_item"),
    path("update/<int:id>/",update,name="update"),
    path('cart_summary/<int:id>/',cart_summary,name="cart_summary"),
    path('view_cart/',view_cart,name="view_cart"),
    path('delete_cart_item/<str:item_id>/',delete_cart_item,name="delete_cart_item"),


    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
