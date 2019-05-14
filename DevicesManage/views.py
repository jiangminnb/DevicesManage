# -*- coding: utf-8 -*-
"""
@author: jiang_min
@contact: jiangminnb@foxmail.com
@version: 1.0
@license: Apache Licence
@file: views.py
"""
from django.shortcuts import render
from QADevices.models import Devices
from django.db.models import Q


def show_moblie_html(request):
    # devices=Devices.objects.all() #将User表中的所有对象赋值给users这个变量，它是一个列表
    # raw_sql = 'select * from "QADevices_devices" where "type"="mobile"'
    # devices = Devices.objects.raw(raw_sql)
    # 过滤 type 为手机的
    devices = Devices.objects.filter(Q(type="mobile") & ~Q(status="company"))
    # 统计个数
    android_conts='Android :' + str(Devices.objects.filter(type="mobile",os='Android').count())  + '台'
    ios_conts = 'iOS : ' + str(Devices.objects.filter(type="mobile",os='iOS').count())  + '台'

    # 生成一个devices变量，这个变量可以给templates中的html文件使用
    return render(request, 'index.html',{'devices':devices,'android_conts':android_conts,'ios_conts':ios_conts})

def search(request):
    q = request.GET.get('q')
    if q:
        devices = Devices.objects.filter(Q(type="mobile",name__icontains=q)|Q(type="mobile",user__icontains=q))
        # devices = Devices.objects.filter().values('name','user')
        android_conts = str(devices.count()) + '  台'
        # 生成一个devices变量，这个变量可以给templates中的html文件使用
        return render(request, 'index.html', {'devices': devices,'android_conts': android_conts})
    else:
        devices = Devices.objects.filter(type="mobile").exclude(status="company")
        # 统计个数
        android_conts = 'Android :' + str(Devices.objects.filter(Q(os='Android') & ~Q(status="company")).count()) + '  台'
        ios_conts = 'iOS : ' + str(Devices.objects.filter(Q(os='iOS') & ~Q(status="company")).count()) + '  台'
        # 生成一个devices变量，这个变量可以给templates中的html文件使用
        return render(request, 'index.html',
                      {'devices': devices, 'android_conts': android_conts, 'ios_conts': ios_conts})

def show_machine_html(request):
    raw_sql='select * from "QADevices_devices" where "type"="machine" and "status"<>"company"'
    devices=Devices.objects.raw(raw_sql)
    # 统计个数
    hp_cont = Devices.objects.filter(Q(brand='琥珀') & ~Q(status="company")).count()
    gz_cont = Devices.objects.filter(Q(brand='公子') & ~Q(status="company")).count()
    xb_cont = Devices.objects.filter(Q(brand='小白') & ~Q(status="company")).count()
    xxb_cont = Devices.objects.filter(Q(brand='小小白') & ~Q(status="company")).count()
    # 生成一个devices变量，这个变量可以给templates中的html文件使用
    return render(request, 'machine.html',{'devices':devices,'hp_cont':hp_cont,'gz_cont':gz_cont,'xb_cont':xb_cont,'xxb_cont':xxb_cont})

def pc(request):
    devices = Devices.objects.filter((Q(type="pc") & ~Q(status="company"))|(Q(type="other") & ~Q(status="company")))
    win_cont = Devices.objects.filter(Q(os='Windows') & ~Q(status="company")).count()
    # 生成一个devices变量，这个变量可以给templates中的html文件使用
    return render(request, 'pc.html',{'devices':devices,'win_cont':win_cont})
