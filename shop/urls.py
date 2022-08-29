"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from store.views import index
from store.views import product_detail, add_to_cart, cart
from shop import settings
from accounts.views import signup
from accounts.views import logout_user
from accounts.views import login_user




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user , name='logout'),
    path('login/', login_user , name='login'),
    path('cart/', cart, name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


