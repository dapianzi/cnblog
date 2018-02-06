import math
from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView, TemplateView
from app.models import Article, Tags, Category
# Create your views here.

class IndexView(TemplateView):
    def get_template_names(self):
        return 'app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 最近3篇文章
        context['posts'] = Article.objects.all().order_by('-pub_time')[:3]
        return context

class PostsView(ListView):
    template_name = 'app/posts.html'
    context_object_name = "article_list"
    page = 1
    max_page = 1
    limit = 6
    name = ''
    cate = ''

    def get_queryset(self, **kwargs):
        # 同时处理按类别和按标签过滤文章，逻辑有点乱
        category = self.request.GET.get('category', '')
        tag = self.request.GET.get('tag', '')
        if '' != tag:
            article_list = Article.objects.filter(tags__name=tag)
            self.cate = 'tag'
            self.name = tag
        elif '' != category:
            article_list = Article.objects.filter(category__name=category)
            self.cate = 'category'
            self.name = category
        else:
            article_list = Article.objects.all()
            self.cate = 'posts'
            self.name = '全部文章'
        qry_set = article_list.select_related('category').prefetch_related('tags').order_by('-pub_time')
        # total page
        total = qry_set.count()
        self.max_page = math.ceil(total / self.limit)
        # current page
        page = self.request.GET.get('page', '')
        self.page = 1 if not page.isdigit() else int(page)
        if self.page < 1 or self.page > self.max_page:
            self.page = 1
        offset = (self.page-1)*self.limit
        return qry_set[offset:offset+self.limit]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # category or tags name
        context['cate_param'] = self.cate
        context['cate_name'] = self.name
        context['page_num'] = self.page
        context['max_page'] = self.max_page
        context['pages'] = range(1 if self.page<5 else self.page-4,
                                 self.max_page+1 if self.page>self.max_page-5 else self.page+5)
        for a in context['article_list']:
            # view summary
            a.summary = a.md_body if len(a.md_body)<=144 else a.md_body[:144]+'...'
        return context

class ArticleView(DetailView):
    model = Article
    template_name = 'app/post.html'
    context_object_name = "post"
    # aid 是urls.py中的正则匹配结果
    pk_url_kwarg = 'aid'

    # 从数据库中获取id为pk_url_kwargs的对象
    def get_object(self, queryset=None):
        obj = super(ArticleView, self).get_object()
        # 点击一次阅读量增加一次
        obj.views += 1
        obj.save()
        return obj

def comment(request, id):
    pass

def sign_in(request):
    pass

def sign_up(request):
    pass

def sign_out(request):
    pass