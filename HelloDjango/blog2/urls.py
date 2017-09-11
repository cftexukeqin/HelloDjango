#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 19:06
# @Author  : DX.Ssssssss
# @Site    : 
# @File    : urls.py
# @Software: PyCharm Community Edition
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
