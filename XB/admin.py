from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.safestring import mark_safe
# 设置admin页面  加入表的字段名
class XBConfig(admin.ModelAdmin):
    def delete(self):
        return mark_safe("<a href="">删除</a>")
    list_display = ["id","name","type","videourl",delete]
    list_filter = ["type"]
    search_fields = ["name"]
admin.site.register(XB,XBConfig)

