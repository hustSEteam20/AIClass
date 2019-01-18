from django.shortcuts import render
from server import models
from AIClass import settings
# Create your views here.


def index(request):
    return render(request, 'server_temp/index.html')


def student_list(request):
    stu_list = []
    if request.method == 'POST':
        id = request.POST.get('stu_id')
        name = request.POST.get('stu_name')
        sex = request.POST.get('stu_sex')
        age = request.POST.get('stu_age')
        print(id, name)
        models.Student.objects.create(stu_id=id, stu_name=name, stu_sex=sex, stu_age=age)
    stu_list = models.Student.objects.all()
    return render(request, 'server_temp/student_tables.html', {'data': stu_list})


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


def teacher_detail(request):
    if request.method == 'GET':
        id = request.GET.get('teacher_id')
        try:
            teacher = models.Teacher.objects.get(teacher_id=id)
            course = teacher.course_set.all()
            course = len(course)
            return render(request, 'server_temp/teacher_detail.html', {'data': teacher, 'course': course})
        except Exception as e:
            return render(request, 'server_temp/error404.html')


def teacher_save(request):
    if request.method == 'POST':
        id = request.POST.get('teacher_id')
        name = request.POST.get('teacher_name')
        sex = request.POST.get('teacher_sex')
        age = request.POST.get('teacher_age')
        pwd = request.POST.get('teacher_pwd')
        try:
            teacher = models.Teacher.objects.get(teacher_id=id)
            teacher.teacher_name = name
            teacher.teacher_sex = sex
            teacher.teacher_age = age
            teacher.teacher_pwd = pwd
            teacher.save()
            teacher_list = models.Teacher.objects.all()  # 查询教师信息
            return render(request, 'server_temp/teacher_tables.html', {'data': teacher_list})
        except Exception as e:
            return render(request, 'server_temp/error404.html')


def teacher_delete(request):
    if request.method == 'GET':
        id = request.GET.get('teacher_id')
    try:
        models.Teacher.objects.filter(teacher_id=id).delete()
        teacher_list = models.Teacher.objects.all()  # 查询教师信息
        return render(request, 'server_temp/teacher_tables.html', {'data': teacher_list})
    except Exception as e:
        return render(request, 'server_temp/error404.html')


def teacher_add(request):
    return render(request, 'server_temp/teacher_add.html')


def course_list(request):
    if request.method == 'POST':
        id = request.POST.get('course_id')
        name = request.POST.get('course_name')
        teacher = request.POST.get('course_teacher')
        time = request.POST.get('course_total')
        models.Course.objects.create(course_id=id, course_name=name, course_teacher=teacher, course_total=time)
    course_list = models.Course.objects.all()  # 查询教师信息
    return render(request, 'server_temp/course_tables.html', {'data': course_list})


def student_detail(request):
    if request.method == "GET":
        id = request.GET.get('stu_id')
        student = models.Student.objects.get(stu_id=id)
        if student:
            return render(request, 'server_temp/student_detail.html', {'data': student})


def student_edit(request):
    if request.method == "POST":
        id = request.POST.get('stu_id')
        name = request.POST.get('stu_name')
        # photo = request.POST.get('stu_photo')
        try:
            photo = request.FILES['stu_photo']
            fname = '%s/img/%s' % (settings.MEDIA_ROOT, photo.name)
            with open(fname, 'wb') as pic:
                for c in photo.chunks():
                    pic.write(c)
            student = models.Student.objects.get(stu_id=id)
            student.stu_img = fname
            student.save()
        except Exception as e:
            pass
        sex = request.POST.get('stu_sex')
        age = request.POST.get('stu_age')
        try:
            student = models.Student.objects.get(stu_id=id)
            student.stu_name = name
            student.stu_sex = sex
            student.stu_age = age
            student.save()
            stu_list = models.Student.objects.all()
            return render(request, 'server_temp/student_tables.html', {'data': stu_list})
        except Exception as e:
            return render(request, 'server_temp/error404.html')




