from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):

    DEPARTMENT_CHOICE = (
        ("1", "应用开发部—测试组"),
        ("2", "应用开发部—开发组"),
        ("3", "其他部门"),
    )

    permanent_asset_number = models.CharField(default='', max_length=50, verbose_name="固定资产编号")
    number = models.CharField(default='', max_length=50, verbose_name="编号")
    mobile_brand = models.CharField(max_length=200, verbose_name="资产名称")
    mobile_model = models.CharField(max_length=200, verbose_name="规格型号")
    configure = models.CharField(default='', max_length=200, verbose_name="配置")
    product_factory = models.CharField(default='', max_length=200, verbose_name="生产厂家")
    price = models.IntegerField(default=0, verbose_name="金额")
    quantity = models.IntegerField(default=0, verbose_name="数量")
    pub_date = models.DateTimeField('借出日期')
    owner = models.CharField(max_length=6, verbose_name="责任人")
    relate_project = models.CharField(default='', max_length=50, verbose_name="关联项目")
    remark = models.CharField(default='', max_length=200, verbose_name="备注")
    email_text = models.EmailField(max_length=254, verbose_name="责任人邮箱")
    is_free = models.BooleanField(verbose_name="闲置")
    # is_free.boolean = True
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICE, verbose_name="责任人部门")
    # serve_time = models.DateField(auto_now_add=True, verbose_name="服役时间")


    def __str__(self):
        return self.mobile_brand

    #用于判断问卷是否最近时间段内发布过
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #将返回布尔值的方法添加一个boolean的属性，并赋值为True，它将显示为on/off的图标，默认显示为True、False
    was_published_recently.boolean = True
    was_published_recently.short_description = u'最近发布'

    class Meta:
        ordering = ["pub_date"]
        verbose_name = "测试手机"
        verbose_name_plural = "测试手机"


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

'''
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
'''