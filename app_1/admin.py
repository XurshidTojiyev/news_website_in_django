from django.contrib import admin

from app_1.models import New


class CreateNew(admin.ModelAdmin):
    list_display = ['news_title', 'news_img', 'news_desc', 'news_tag']
admin.site.register(New, CreateNew)