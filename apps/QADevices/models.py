from django.db import models

# Create your models here.
from datetime import datetime

from django.utils.html import format_html

class Devices(models.Model):
    TYPE_CHOICES=(
        ("mobile", u"手机"),
        ("machine", u"机器"),
        ("pc", u"电脑#显示器"),
        ("other", u"其他")
    )

    OS_CHOICES=(
        ("Android","Android"),
        ("iOS", "iOS"),
        ("Windows", "Windows"),
        ("Linux", "Linux"),
        ("Mac", "Mac"),
        ("Other","Other")

    )

    STATUS_CHOICES=(
        ("lend", u"借出"),
        ("idle", u"闲置"),
        ("company", u"已还公司")
    )
    name = models.CharField(max_length=50, verbose_name='设备名称')
    type = models.CharField(max_length=10,choices=TYPE_CHOICES,verbose_name='设备类型',default='machine')
    os = models.CharField(max_length=50,choices=OS_CHOICES, verbose_name='操作系统',default='Android')
    version = models.CharField(max_length=50,verbose_name='版本',default='v1.0.0')
    sn = models.CharField(max_length=50,null=True, blank=True, verbose_name='设备编号')
    macid = models.CharField(max_length=50, null=True, blank=True, verbose_name='设备标识')
    brand = models.CharField(max_length=50,null=True, blank=True, verbose_name='品牌')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,verbose_name='状态')
    owner = models.CharField(max_length=50,verbose_name='拥有者')
    user = models.CharField(max_length=50,null=True, blank=True, verbose_name='借用人')
    configuration = models.TextField(null=True,blank=True, verbose_name='详细配置')
    remarks = models.CharField(max_length=100, null=True,blank=True, verbose_name='备注')
    add_time = models.DateTimeField(null=True,blank=True,verbose_name='借出时间',)

    '''
    verbose_name=u"解释"   # 显示名称
    null=True     # 可以为空
    blank=True    # 是否必填
    '''

    # 不同 状态 显示不同颜色
    def status_color(self):
        if self.status == 'lend':
            # color = '#00F'
            color = 'green'
            verbose_name = u'借出'
        elif self.status == 'idle':
            # color = '#F00'
            color='red'
            verbose_name = u'闲置'
        elif self.status == 'company':
            # color = '#F00'
            color='grey'
            verbose_name = u'已还公司'
        else:
            color = 'grey'
            verbose_name = self.status
        return format_html(
            '<span style="color: {}">{}</span>',
            color,
            verbose_name,
        )

    def os_icon(self):
        if self.os == 'Android':
            classes = 'fa fa-android'
            color = 'green'
        elif self.os == 'iOS':
            classes = 'fa fa-apple'
            color = ''
        elif self.os =='Linux':
            classes ='fa fa-linux'
            color = ''
        elif self.os =='Windows':
            classes ='fa fa-windows'
            color = ''
        else:
            classes = ''
            color = ''
        return format_html(
            '<span class="{}" style="color:{}"> {} </span>',
            classes,
            color,
            self.os,
        )

    # 标题栏显示
    status_color.short_description = u"状态"
    os_icon.short_description = u"操作系统"

    class Meta:
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name