from django.db import models

# Create your models here.
#创建数据表用，建表时候通常第一个字母大写
#商品类别表
class Type(models.Model):
    class Meta:
        verbose_name='商品类别'#单数形式
        verbose_name_plural = '商品类别'  #复数形式
    type_name=models.CharField(max_length=50,verbose_name='类名')

    def __str__(self):   #在调用的时候返回名称
        return self.type_name

#商品表
class Goods(models.Model):
    class Meta:
        verbose_name='商品'#单数形式
        verbose_name_plural = '商品'  #复数形式
    goods_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/image')
    price=models.FloatField()
    is_delete=models.IntegerField(default=1) #1代表上架，0代表下架

#关系表,关联表数据删除的时候要先删除主表数据然后才能删除从表的数据
class Goods_type(models.Model):
    class Meta:
        verbose_name='商品分类表'#单数形式
        verbose_name_plural = '商品分类表'  #复数形式
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE)
    type=models.ForeignKey(to='Type',on_delete=models.CASCADE)