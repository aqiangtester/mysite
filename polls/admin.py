from django.contrib import admin
from .models import Question, Choice
# Register your models here.

admin.site.site_header = "测试资产管理系统"
admin.site.site_title = "测试资产"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # inlines = [ChoiceInline]
    fieldsets = [
        (
            "机器信息", {
                "fields": [
                    'permanent_asset_number', 'number', "mobile_brand", "mobile_model",
                    'configure', 'product_factory', 'price', 'quantity', 'relate_project', 'remark'
                ]
            }
        ),
        (
            "人员详情", {
                "fields": ["pub_date", "owner", "department", "email_text", "is_free"],
                # "classes": ["collapse"],
            },
        ),
        # (
        #     "选项", {
        #         "fields": [ChoiceInline]
        #     }
        # )
        # ("详细",{"fields":["pub_date", "email_text"], "classes":["collapse"]}),
    ]

    #在question列表增加显示下列字段
    list_display = (
        'permanent_asset_number', 'number', "mobile_brand", "mobile_model",  'configure', 'product_factory',
        'price', 'quantity', 'relate_project',"pub_date", "owner", "department", "email_text", "is_free",
    )

    ''''
    说明：指定在list_display属性中列出的字段，作为超链接至修改页面的字段
    要求：此属性依赖list_display属性，必须要有list_display
    '''
    list_display_links = ("mobile_brand",)

    '''
    说明：定义可以直接在列表修改的字段，
    要求：1、不能定义list_display中没有的字段
          2、不能定义list_display_links中已有的字段  
    '''
    list_editable = ("pub_date", "owner", "is_free", "department")

    #在列表右侧增加过滤字段
    list_filter = ["owner"]

    '''
    说明：设置一个列表显示的数据最大条数，默认为200
    '''
    list_max_show_all = 10

    '''
    说明：设置每页显示多少个数据，默认100
    '''
    list_per_page = 5

    # show_full_result_count = False
    view_on_site = False

    #增加查询条件
    search_fields = ["mobile_brand"]

    date_hierarchy = 'pub_date'


# admin.site.register(Question, QuestionAdmin)