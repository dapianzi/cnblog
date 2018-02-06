# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

from markdownx.models import MarkdownxField


# Create your models here.

class Article(models.Model):
    """博文文章"""
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    pub_time = models.DateTimeField('发表时间', db_index=True, auto_now_add=True)
    title = models.CharField('标题', max_length=100, default='')
    md_body = MarkdownxField('MD内容', default='')
    html_body = models.TextField('HTML内容', default='')
    tags = models.ManyToManyField(
        'Tags',
        verbose_name='文章标签',
        related_name='article_tags'
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='文章类别',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    from_url = models.CharField(default='', max_length=250)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def pub_time_format(self):
        """自定义字段，增加可读性"""
        return self.pub_time.strftime("%Y-%m-%d %H:%M:%S")

class Category(models.Model):
    """文章类别"""
    name = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name

class Tags(models.Model):
    """文章标签"""
    name = models.CharField(max_length=50, default='')

    def mod(self):
        return self.id%5

    def __str__(self):
        return self.name

class Comments(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'Guests',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    pub_time = models.DateTimeField('评论时间', auto_now_add=True)
    comment = models.CharField(max_length=1024, default='')
    reply_to = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    def __str__(self):
        return self.author

class Guests(models.Model):
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50, default='')
    token = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name

class Config(models.Model):
    conf_key = models.CharField(max_length=50, default='')
    conf_str = models.CharField(max_length=50, default='')
    conf_int = models.IntegerField(default=0)
    def __str__(self):
        return self.conf_key
