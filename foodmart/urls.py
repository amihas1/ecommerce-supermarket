from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('category/<categoryname>', views.category, name='category'),
    path('item/<pk>', views.item, name='item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)