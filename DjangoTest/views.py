from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponse('Hello world!')

# def login(request):
#     a1="<a href='https://www.baidu.com/'>百度"
#     a2="<a href='baidu.com/'>百度"
#     return HttpResponse(a1)

def login(request):
    a="<a href='https://www.baidu.com/'>百度"
    username=request.GET.get('username')
    pwd=request.GET.get('password')
    print(username,pwd)
    return render(request,'login.html',{"a": a})

def show_index(request):
    return render(request,'index.html',{'index':"首页"})

def loginp(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        print(username,pwd)
        if username=='admin' and pwd=='admin':
            return HttpResponseRedirect('/show index')
        return render(request,'login.html')

def register(request):
    # print("request",request)
    if request.method=='POST':
        print(111111111)
        username=request.POST.get('name','admin')
        pwd=request.POST.get('password')
        return HttpResponseRedirect('/login')
    return render(request,'register.html')

def list(request):
    list1=[1,2,3,4,5]
    return render(request,'list.html',locals())