from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# Create your views here.

def home(request):
    return render(request, 'home.html')


def book_list(request):
    # 把图书全部查询出来然后传递给html界面
    query_set = models.Book.objects.all()
    return render(request, 'book.html', locals())


def book_add(request):
    # 获取从前端传回的数据
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')

        # 操作数据库
        # 书籍表
        book_obj = models.Book.objects.create(title=title, price=price,
                                              publish_date=publish_date,
                                              publish_id=publish_id)
        # 书籍与作者关系表
        # create 会返回一个值，通过这个值来进行添加作者列表，将其打散
        book_obj.authors.add(*authors_list)
        """
        redirect中可以直接写url 也可以写别名
        但是别名需要额外给参数了就要使用reverse进行反向解析
        """
        return redirect('book_list')

    # 把出版社信息和作者信息全部获取到
    publish_queryset = models.Publish.objects.all()
    authors_queryset = models.Author.objects.all()
    # 通过locals传递给html界面
    return render(request, 'book_add.html', locals())


def book_edit(request, edit_id):
    # 获取用户想要编辑的书籍对象，展示给用户看
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    # 获取从前端传回的数据
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        models.Book.objects.filter(pk=edit_id).update(title=title,
                                                      price=price,
                                                      publish_id=publish_id,
                                                      publish_date=publish_date)
        # 第三章关系表
        edit_obj.authors.set(authors_list)
        return redirect('book_list')

    publish_queryset = models.Publish.objects.all()
    authors_queryset = models.Author.objects.all()
    return render(request, 'book_edit.html', locals())


def delete(request, delete_id):
    # 直接删除
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect('book_list')