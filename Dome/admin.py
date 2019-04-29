from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.safestring import mark_safe

class powerquestionbankConfig(admin.ModelAdmin):
    def delete(self):
        return mark_safe("<a href="">删除</a>")

    list_display = ["rubric","answer","option",delete]
    search_fields = ["rubric"]

admin.site.register(powerquestionbank,powerquestionbankConfig)

class MessageConfig(admin.ModelAdmin):

    search_fields = ["user"]
admin.site.register(Message, MessageConfig)