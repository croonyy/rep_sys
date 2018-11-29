# encoding:utf-8

from functools import wraps
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


# 登录限制装饰器,作用是如在未登录的状态用到需要登录的功能则首先跳到登录页面
# def login_required(func):
#     @wraps(func)
#     def wrapper(request,*args, **kwargs):
#         u = request.session.has_key('username')
#         return func(*args, **kwargs)
#         pass
def login_required(func):
    # '''自定义 登录验证 装饰器'''
    @wraps(func)
    def check_login_status(request, *args, **kwargs):
        # '''检查登录状态'''
        if request.session.has_key('username'):
            # 当前有用户登录，正常跳转
            return func(request, *args, **kwargs)
        else:
            # 当前没有用户登录，跳转到登录页面
            return redirect(reverse('login'))

    return check_login_status
