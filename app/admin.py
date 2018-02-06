from django.contrib import admin
from django.utils.html import format_html

from markdownx.admin import MarkdownxModelAdmin
from app.models import Article, Comments, Tags, Category, Guests, Config

# Register your models here.
# 注册一些全局属性
admin.site.empty_value_display = '(不存在)'

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('conf_key', 'conf_int', 'conf_str')

@admin.register(Article)
class ArticleAdmin(MarkdownxModelAdmin):
    # 列表页展示的字段
    list_display = ('title', 'pub_time', 'category', 'tags_list', 'views')
    # 可直接在列表页编辑的字段
    list_editable = ['views']
    # 定义跳转detail的链接绑定到哪个字段，默认第一个
    list_display_links = ['title']
    # 右侧快捷筛选菜单
    list_filter = ['category', 'tags']
    # 详情页编辑显示的字段
    fields = (('title', 'category'), 'md_body', 'tags', )
    # 优化多对多字段显示
    filter_horizontal = ('tags', )
    # date_hierarchy = 'pub_time'
    # form = ArticleForm
    # def get_readonly_fields(self, request, obj=None):
    #     # 对于只读字段，在详情编辑页显示
    #     if obj:
    #         return ('pub_time',)
    #     else:
    #         # 添加时
    #         return ()

    def tags_list(self, obj):
        """自定义列"""
        s = []
        for t in obj.tags.all():
            s.append('<span class="label label-primary">%s</span>' % t.name)
        return format_html(' '.join(s))
    tags_list.short_description = '标签'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pwd')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', )
