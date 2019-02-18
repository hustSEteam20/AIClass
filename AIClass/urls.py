"""AIClass URL Configuration

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
from server import views

from django.views.static import serve
from AIClass.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('index/', views.index),
    url('student_list/', views.student_list),
    url('teacher_list/', views.teacher_list),
    url('teacher_detail/', views.teacher_detail),
    url('teacher_save/', views.teacher_save),
    url('teacher_add/', views.teacher_add),
    url('teacher_delete/', views.teacher_delete),
    url('course_list/', views.course_list),
    url('student_detail/', views.student_detail),
    url('stu_edit/', views.student_edit),
    url('student_delete', views.student_delete),
    url('student_add', views.student_add),
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT})
]
