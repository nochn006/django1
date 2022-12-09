from django.contrib import admin
from django.urls import path

from Rostislav import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, kwargs = {'name': 'Rostislav', 'fname': 'Ryasik', }),
    path('about', views.about, kwargs = {'about': 'Приехал из Республики Крым'}),
    path('contact', views.contact, kwargs = {'phone': '+79270415709'}),

]
