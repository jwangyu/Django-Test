from django.shortcuts import render
from .models import Type
# Create your views here.
def index(request):
    return render(request, 'changed/index.html')

def base(request):
    return render(request,'base/base.base.html')

def demo(request):
    return render(request, 'base/demo.html')

# def base1(request):
#     return render(request,'base1/base.html')

def pinpai(request):
    return render(request, 'changed/pinpai.html')

def meishi(request):
    type_list=Type.objects.all()
    # print(type_list,type(type_list))
    # for t in type_list:
    #     print(t.type_name,t.id)
    return render(request, 'changed/meishi.html',{'type_list': type_list})


def shop(request):
    return render(request, 'changed/shop.html')

def news(request):
    return render(request, 'changed/news.html')

def about_us(request):
    return render(request, 'changed/about-us.html')