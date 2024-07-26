
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

from . import views

from django.contrib import admin
from django.urls import path
# urls.py
from Second.views import home, menu, edit, create, delete, order_food

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('menu/', menu, name='menu'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('order/<int:pk>/', order_food, name='order_food'),
    path('orders/', views.order_list, name='order_list'),  # Add this line

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

