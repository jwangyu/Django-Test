from django.contrib import admin
from .models import Type,Goods,Goods_type

# Register your models here.
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type_name','id']
    ordering = ['id']   #排序方式 -id是倒叙方式

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods_name','image','price','is_delete']

@admin.register(Goods_type)
class Goods_TypeAdmin(admin.ModelAdmin):
    list_display = ['goods','type']