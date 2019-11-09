from django.db import models

# Create your models here.
#创建数据表用，建表时候通常第一个字母大写
#商品类别表
class Type(models.Model):
    class Meta:
        verbose_name='商品类别'#单数形式
        verbose_name_plural = '商品类别'  #复数形式
        ordering=['-id']#按照ID的倒序排，优先级小于views的优先级
    type_name=models.CharField(max_length=50,verbose_name='类名')

    def __str__(self):   #在调用的时候返回名称
        return self.type_name

#商品表
class Goods(models.Model):
    class Meta:
        verbose_name='商品'#单数形式
        verbose_name_plural = '商品'  #复数形式
    goods_name=models.CharField(max_length=50,verbose_name='商品名称')
    image=models.ImageField(upload_to='media/image',verbose_name='图片')
    price=models.FloatField('价钱',blank=True,null=True)#blank为true表示可以为空，为false表示必填项不能为空，一般默认false，null为true是代表为空的时候用null填充，默认fasle不为空
    is_delete=models.IntegerField(default=1,verbose_name='是否下架') #1代表上架，0代表下架
    def __str__(self):#这个的作用是在添加完成后上传的时候显示xx名称的物品已经上传，如果不写这个这显示objectxx已上传
        return self.goods_name

#关系表,关联表数据删除的时候要先删除主表数据然后才能删除从表的数据
class Goods_type(models.Model):
    class Meta:
        verbose_name='商品分类表'#单数形式
        verbose_name_plural = '商品分类表'  #复数形式
    goods=models.ForeignKey(to='Goods',on_delete=models.CASCADE)
    type=models.ForeignKey(to='Type',on_delete=models.CASCADE)