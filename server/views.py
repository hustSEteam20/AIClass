from django.shortcuts import render
from django.template import RequestContext
from server import models
# Create your views here.


def index(request):
    return render(request, 'server_temp/index.html')


def student_list(request):
    user_list = []
    if request.method == 'POST':
        id = request.POST.get('stu_id')
        name = request.POST.get('stu_name')
        sex = request.POST.get('stu_sex')
        age = request.POST.get('stu_age')
        print(id, name)
        models.Student.objects.create(stu_id=id, stu_name=name, stu_sex=sex, stu_age=age)
    user_list = models.Student.objects.all()
    return render(request, 'server_temp/student_tables.html', {'data': user_list})


def teacher_list(request):
    if request.method == 'POST':
        id = request.POST.get('teacher_id')
        name = request.POST.get('teacher_name')
        pwd = request.POST.get('teacher_pwd')
        sex = request.POST.get('teacher_sex')
        age = request.POST.get('teacher_age')
        models.Teacher.objects.create(teacher_id=id, teacher_name=name, teacher_pwd=pwd,
                                      teacher_sex=sex, teacher_age=age)
    teacher_list = models.Teacher.objects.all()  # 查询教师信息
    return render(request, 'server_temp/teacher_tables.html', {'data': teacher_list})


def course_list(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        teacher = request.POST.get('course_teacher')
        time = request.POST.get('course_total')
        models.Course.objects.create(course_id=id, course_name=name, course_teacher=teacher, course_total=time)
    course_list = models.Course.objects.all()  # 查询教师信息
    return render(request, 'server_temp/course_tables.html', {'data': course_list})





