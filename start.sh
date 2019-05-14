#!/bin/bash

#author: jiang_min
#contact: jiang_min@gowild.cn
#version: 1.0
#license: Apache Licence
#time: 2018/10/31 17:00
cd /data/MyDevicesManage/
source /opt/py3/bin/activate
python manage.py runserver 172.27.1.18:5000
