from django.shortcuts import render
from server import models
from AIClass import settings
import os
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


def student_detail(request):
    if request.method == "GET":
        id = request.GET.get('stu_id')
        student = models.Student.objects.get(stu_id=id)
        if student:
            return render(request, 'server_temp/student_detail.html', {'data': student})


def student_delete(request):
    if request.method == 'GET':
        id = request.GET.get('stu_id')
    try:
        student = models.Student.objects.get(stu_id=id)
        print(student.stu_img.name)
        img_url = student.stu_img.name
        print(img_url)
        # url = ''
        # for i in range(len(img_url)-1):
        #     print(url)
        #     url += (img_url[i]+'\\')
        # url += img_url[-1]
        # print(url)
        # img_url = img_url.replace(r'\','\\')
        models.Student.objects.filter(stu_id=id).delete()
        os.remove(img_url)
        student_list = models.Student.objects.all()  # 查询教师信息
        return render(request, 'server_temp/student_tables.html', {'data': student_list})
    except Exception as e:
        return render(request, 'server_temp/error404.html')


def student_add(request):
    return render(request, 'server_temp/student_add.html')


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
    try:
        course_list = models.Course.objects.all()
        detail_list = {}
        att_list = []
        ans_list = []
        c_list = []
        for course in course_list:  # 每种课
            detail_list = {}
            ans_detail_list = {}
            c_list.append(course.course_name)
            course_detail_list = models.CourseDetail.objects.filter(course_id_id=course.course_id)  # 每个人课程详细
            student_sum = len(models.CourseSelection.objects.filter(course_id=course.course_id))
            course_dict = {
                'name': course.course_name,
                'type': 'line',
                'data': []
            }
            ans_dict = {
                'name': course.course_name,
                'type': 'line',
                'data': []
            }
            for detail in course_detail_list:  # 每条记录
                if detail.course_time not in detail_list:
                    detail_list[detail.course_time] = 0
                    ans_detail_list[detail.course_time] = 0
                if detail.detail_attendance:
                    detail_list[detail.course_time] += 1
                ans_detail_list[detail.course_time] += detail.detail_answer



                # detail_list[detail.course_time]['detail_answer'] += detail.detail_answer
            for detail in detail_list:
                # detail_list[detail] /= student_sum * 0.01
                course_dict['data'].append(detail_list[detail] / student_sum * 100)
                ans_dict['data'].append(ans_detail_list[detail] / student_sum * 100)
                # detail_list[detail]['detail_answer'] /= student_sum * 0.01
            att_list.append(course_dict)
            ans_list.append(ans_dict)
        print(att_list)
        return render(request, 'server_temp/course_tables.html', {'e_chart': att_list, 'e_chart2': ans_list,
                                                                  'data': course_list, 'c_list': c_list})
    except Exception as e:
        return render(request, 'server_temp/error404.html')
    '''
    try:
        course_list = models.Course.objects.all()
        detail_list = {course.course_name: {} for course in course_list}
        for course in course_list:
            course_detail_list = models.CourseDetail.objects.filter(course_id_id=course.course_id)
            student_sum = len(models.CourseSelection.objects.filter(course_id=course.course_id))
            for detail in course_detail_list:
                if detail.course_time not in detail_list[course.course_name]:
                    detail_list[course.course_name][detail.course_time] = {'attendance_sum': 0, 'detail_answer': 0}
                    # detail_list[course.course_name] = {detail.course_time: {'attendance_sum': 0, 'detail_answer': 0}}
                if detail.detail_attendance:
                    detail_list[course.course_name][detail.course_time]['attendance_sum'] += 1
                detail_list[course.course_name][detail.course_time]['detail_answer'] += detail.detail_answer
            for detail in detail_list[course.course_name]:
                detail_list[course.course_name][detail]['attendance_sum'] /= student_sum * 0.01
                detail_list[course.course_name][detail]['detail_answer'] /= student_sum * 0.01
        return render(request, 'server_temp/course_tables.html', {'e_chart': detail_list, 'data': course_list})
    except Exception as e:
        return render(request, 'server_temp/error404.html')
    course_list = models.Course.objects.all() 
    return render(request, 'server_temp/course_tables.html', {'data': course_list})'''


def course_detail(request):
    if request.method == 'GET':
        id = request.GET.get('course_id')
        print(type(id))
        print(id)
        try:
            course_detail_list = models.CourseDetail.objects.filter(course_id_id=id)
            student_sum = len(models.CourseSelection.objects.filter(course_id=id))
            print(student_sum)
            detail_list = {}
            for detail in course_detail_list:
                if detail.course_time not in detail_list:
                    detail_list[detail.course_time] = {'attendance_sum': 0, 'detail_answer': 0}
                if detail.detail_attendance:
                    detail_list[detail.course_time]['attendance_sum'] += 1
                detail_list[detail.course_time]['detail_answer'] += detail.detail_answer
            for detail in detail_list:
                detail_list[detail]['attendance_sum'] /= student_sum * 0.01
                detail_list[detail]['detail_answer'] /= student_sum * 0.01
            return render(request, 'server_temp/course_detail.html', {'data': detail_list, 'course_id': id})
        except Exception as e:
            return render(request, 'server_temp/error404.html')

def echart_detail(request):
        '''try:
            course_list = models.Course.objects.all()
            detail_list = {}
            c_list = []
            for course in course_list:
                c_list.append(course.course_name)
                course_detail_list = models.CourseDetail.objects.filter(course_id_id=course.course_id)
                student_sum = len(models.CourseSelection.objects.filter(course_id=course.course_id))
                for detail in course_detail_list:
                    if detail.course_time not in detail_list:
                        detail_list[course][detail.course_time] = {'attendance_sum': 0, 'detail_answer': 0}
                    if detail.detail_attendance:
                        detail_list[course][detail.course_time]['attendance_sum'] += 1
                    detail_list[course][detail.course_time]['detail_answer'] += detail.detail_answer
                for detail in detail_list:
                    detail_list[course][detail]['attendance_sum'] /= student_sum * 0.01
                    detail_list[course][detail]['detail_answer'] /= student_sum * 0.01

            return render(request, 'server_temp/course_tables.html', {'e_chart': detail_list})
        except Exception as e:
            return render(request, 'server_temp/error404.html')'''
        try:
            course_list = models.Course.objects.all()
            detail_list = {}
            att_list = []
            ans_list = []
            c_list = []
            for course in course_list:   # 每种课
                detail_list = {}
                c_list.append(course.course_name)
                course_detail_list = models.CourseDetail.objects.filter(course_id_id=course.course_id)     # 每个人课程详细
                student_sum = len(models.CourseSelection.objects.filter(course_id=course.course_id))
                course_dict = {
                    'name': course.course_name,
                    'type': 'line',
                    'data': []
                }
                for detail in course_detail_list:   # 每条记录
                    if detail.course_time not in detail_list:
                        detail_list[detail.course_time] = 0
                    if detail.detail_attendance:
                        detail_list[detail.course_time] += 1
                    # detail_list[detail.course_time]['detail_answer'] += detail.detail_answer
                for detail in detail_list:
                    # detail_list[detail] /= student_sum * 0.01
                    course_dict['data'].append(detail_list[detail]/student_sum*100)
                    # detail_list[detail]['detail_answer'] /= student_sum * 0.01
                att_list.append(course_dict)
            print(att_list)
            return render(request, 'server_temp/course_tables.html', {'e_chart': att_list})
        except Exception as e:
            return render(request, 'server_temp/error404.html')



def course_detail_period(request):
    if request.method == 'GET':
        course_id = request.GET.get('course_id')
        period_id = request.GET.get('period_id')
        #print(type(id))
        #print(id)
        try:
            course_detail_list = models.CourseDetail.objects.filter(course_id=course_id,course_time=period_id)
            print(course_detail_list)
            # detail_list = {}
            # for detail in course_detail_list:
            #     if detail.course_time not in detail_list:
            #         detail_list[detail.course_time] = {'attendance_sum': 0, 'detail_answer': 0}
            #     detail_list[detail.course_time]['attendance_sum'] += 1
            #     detail_list[detail.course_time]['detail_answer'] += detail.detail_answer
            # for detail in detail_list:
            #     detail_list[detail]['attendance_sum'] /= student_sum * 0.01
            #     detail_list[detail]['detail_answer'] /= student_sum * 0.01
            return render(request, 'server_temp/course_detail_period.html', {'data': course_detail_list, 'course_id':course_id})
        except Exception as e:
            return render(request, 'server_temp/error404.html')


def course_selection(request):
    try:
        course_list = models.Course.objects.all()
        student_list = models.Student.objects.all()
        return render(request, 'server_temp/course_select.html', {'course': course_list, 'student': student_list})
    except Exception as e:
        return render(request, 'server_temp/error404.html')


def select_course(request):
    if request.method == 'POST':
        s_id = request.POST.get("s_id")
        c_id = request.POST.get("c_id")
        models.CourseSelection.objects.create(course_id_id=c_id, stu_id_id=s_id)
        return render(request, 'server_temp/select_suc.html')
    else:
        course_list = models.Course.objects.all()
        student_list = models.Student.objects.all()
        return render(request, 'server_temp/course_select.html', {'course': course_list, 'student': student_list})





