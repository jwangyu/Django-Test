from django.shortcuts import render
from .models import Type,Goods
from django.http import Http404

# Create your views here.
def index(request):
    index='nav-active' #给每个页面都添加一个参数{{}}，并在return中通过字典的形式将值传进去。
    return render(request, 'changed/index.html',{'index':index})

def base(request):
    return render(request,'base/base.base.html')

def demo(request):
    return render(request, 'base/demo.html')

# def base1(request):
#     return render(request,'base1/base.html')

def pinpai(request):
    pinpai='nav-active'
    return render(request, 'changed/pinpai.html',{"pinpai":pinpai})

def meishi(request):
    meishi='nav-active'
    type_list=Type.objects.all()
    # type_list=Type.objects.filter(id=3,type_name='风味') #条件查询，返回的也是一个结果集，多个条件时是且的关系
    # type_list=Type.objects.get(id=7) #获取到单个对象，当数据不存在时会报错。
    # type_list=Type.objects.exclude(id=3) #排除符合条件的数据
    # type_list=Type.objects.exclude(id=3).exclude(type_name='酒水饮料')#想排除删掉多个条件数据时，使用多个exclude
    # type_list=Type.objects.filter(id__lt=9) #小于
    # type_list=Type.objects.filter(id__lte=9) #小于等于
    # type_list=Type.objects.filter(id__gt=3) #大于
    # type_list=Type.objects.filter(id__gte=3) #大于等于
    # type_list=Type.objects.filter(id__in=[7,10]) #列表内数据中取值第7个和第10个
    # type_list=Type.objects.filter(type_name__contains='食')#模糊查询
    # type_list=Type.objects.filter(type_name__endswith="物") #以。。。结尾
    # type_list=Type.objects.filter(type_name__startswith='物')#以。。。开头
    type_list=Type.objects.order_by('id') #对数据进行排序，优先级别高于models中的优先级。如果同时设置了则以这里的为准
    if type_list.exists(): #和上边查找的同时使用
        print('有数据')
    else:
        print('无数据')
    for t in type_list:
        goods_type_list=t.goods_type_set.all()
        for g in goods_type_list:
            print(g.goods.id,g.goods.goods_name,g.goods.price,t)
            #查询外键关联的表数据，主表数据.小写的从表表名——set.all()
            #从表(关联表）查主表的数据：从表数据.外键主表表名.外键主表字段名

    # print(type_list,type(type_list))
    for t in type_list:
        print(t.type_name,t.id)
    return render(request, 'changed/meishi.html',{'type_list': type_list},{'meishi':meishi})


def shop(request):
    shop='nav-active'
    return render(request, 'changed/shop.html',{'shop':shop})

def news(request):
    news='nav-active'
    return render(request, 'changed/news.html',{'news':news})

def about_us(request):
    about_us='nav-active'
    return render(request, 'changed/about-us.html',{'about_us':about_us})

def meishi_detail(request,id):
    goods=Goods.objects.filter(id = id)
    if goods.exists():
        good=goods[0]
    else:
        raise Http404
    print(id,"1111111111")
    return render(request,'new_html/meishi-con.html',{'good':good})