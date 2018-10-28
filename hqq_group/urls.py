# -*- coding: utf-8 -*-
# __author__= "Ruda"
# Data: 2018/10/21

from django.urls import path
from hqq_group import views

version_1 = 'v1/'
'''
2018年9月份开始的版本
初创版
亟待优化重构
'''

urlpatterns = [
    path(version_1 + 'add/', views.Add.as_view()),
    path(version_1 + 'join/', views.Join.as_view()),
    path(version_1 + 'exit/', views.Exit.as_view()),

]
