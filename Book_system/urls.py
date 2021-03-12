"""Book_system URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页    使用反向解析
    url(r'^$', views.home, name='home'),
    # 图书列表
    url(r'^book/list/', views.book_list, name='book_list'),
    # 添加书籍
    url(r'^book/add/', views.book_add, name='book_add'),
    # 编辑书籍  使用有名分组
    url(r'^book/edit/(?P<edit_id>\d+)/', views.book_edit, name='book_edit'),
    # 删除书籍 使用无名分组
    url(r'^book/delete/(\d+)/', views.delete, name='book_delete')

]
