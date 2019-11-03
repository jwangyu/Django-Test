
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('pinpai/', views.pinpai,name='pinpai'),
    path('meishi/', views.meishi,name='meishi'),
    path('shop/',views.shop,name='shop'),
    path('news/',views.news,name='news'),
    path('about_us/',views.about_us,name='about_us'),
    path('base/',views.base,name='base'),
    path('demo/',views.demo,name='demo'),
    # path('base1/', views.base1, name='base1')

]
app_name='meishi'