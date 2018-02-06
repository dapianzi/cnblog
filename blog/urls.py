"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^blog/dapianzi-admin/', admin.site.urls),
    url(r'^blog/', include('app.urls', namespace='blog')),
    url(r'^blog/markdownx/', include('markdownx.urls', namespace='md')),
]
if settings.DEBUG:
    # todo 配置 admin 后台markdown编辑器上传图片
    media_root = os.path.join(settings.BASE_DIR,'media')
    urlpatterns += static('/blog/data/', document_root=media_root)