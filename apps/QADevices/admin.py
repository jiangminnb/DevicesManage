from __future__ import absolute_import
# Register your models here.
import xadmin
from xadmin import  views
from .models import Devices

# Register your models here.

# 开启后台主题样式选择
class BaseSetting(object):
    # enable_themes = True   # 切换主题
    use_bootswatch = True

# 全局设置
class GlobalSettings(object):
    """标题及版权修改"""
    site_title = "江敏日进斗金系统"

    site_footer = "2018-2019 JiangMin"  # 页脚版权

    # menu_style = "accordion"   # 左侧导航收缩模式

# 修改登录界面显示
class LoginSetting(object):
    title="日进斗金系统"

class DevicesAdmin(object):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','name','os_icon','version','sn','macid','brand','status_color','owner','user')

    # 修改图标 http://fontawesome.io/icons/
    # xadmin/static/xadmin/vendor/font-awesome
    model_icon = 'fa fa-mobile-phone'

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)
    # ordering = ('-id',)

    # list_editable 设置默认可编辑字段,弹出编辑框
    list_editable = ['status_color',]

    # 仅可读，不可编辑
    readonly_fields =['id',]

    #fk_fields 设置显示外键字段
    # fk_fields = ('name',)

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name')

    # 筛选器
    list_filter = ('type','os','status','owner')
    search_fields = ('name','brand','user')  # 搜索字段
    # date_hierarchy = 'go_time'  # 详细时间分层筛选

# 注册到后台
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.LoginView,LoginSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(Devices,DevicesAdmin)
