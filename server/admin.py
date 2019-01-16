from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
# Register your models here.

from . import models
# admin.site.register(models.Student)
# admin.site.register(models.Course)
admin.site.register(models.Selection)
# admin.site.register(models.Summary)
admin.site.register(models.Teacher)


class Find(admin.SimpleListFilter):

    title = _('number')
    parameter_name = 'stu_id'

    def lookups(self, request, model_admin):
        return (
            ('M20180001', _('maziheng')),
            ('M20180002', _('zhaolu'))
        )

    def queryset(self, request, queryset):
        if (self.value()) == 'M20180001':
            # return queryset.filter(models.Student.stu_id == 'M20180001')
            return models.Summary.objects.filter(Q(stu_id='M20180001'), Q(interaction=1))
        if(self.value()) == 'M20180002':
            return models.Summary.objects.filter(Q(stu_id='M20180002'))



@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'stu_name', 'condition')

    list_filter = ('stu_id', 'stu_name')



    def cond(self, obj):
        models.con()

    # class MyAdminSite(admin.AdminSite):
#     site_header = 'AIClass'  # 此处设置页面显示标题
#     site_title = 'AIClass Login'  # 此处设置页面头部标题


@admin.register(models.Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('stu_id_id', 'course_id_id', 'attendance',
                    'interaction', 'grade', 'course_time')
    list_filter = (Find,)
    # list_display = ('condi',)



    def get_res(self, obj):
        if obj.stu_id == 'M20180001':
            return obj


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name')

    # def detail(self, obj):
       # return '%s' % obj.



admin.site.site_header = 'AI大课堂后台登录'
admin.site.site_title = 'AI大课堂后台系统'
# admin_site = MyAdminSite(name='server_temp')



