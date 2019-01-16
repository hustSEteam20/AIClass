from django.db import models
from django.db.models import Q
# Create your models here.

#
# class Student(models.Model):
#     gender = (
#         ('male', "男"),
#         ('female', "女"),
#     )
#     stu_id = models.CharField(max_length=128, unique=True, primary_key=True)
#     stu_name = models.CharField(max_length=128)
#     stu_photo = models.ImageField(upload_to='media',null=True)
#     stu_sex = models.CharField(max_length=32, choices=gender, default='男')
#     stu_age = models.IntegerField(null=True)
#
#     def __str__(self):
#         return str(self.stu_id)
#
#     def condition(self):
#         if self.stu_id == 'M20180001':
#             return 'yes'
#         # 照片路径
#
#
# class Teacher(models.Model):
#     teacher_id = models.CharField(max_length=128, unique=True, primary_key=True)
#     teacher_name = models.CharField(max_length=128)
#     teacher_pwd = models.CharField(max_length=128)
#
#
# class Course(models.Model):
#     course_id = models.CharField(max_length=128, unique=True, primary_key=True)
#     course_name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return str(self.course_id)
#
#
#
# class Summary(models.Model):
#     sum_id = models.AutoField(primary_key=True)
#     course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
#     attendance = models.IntegerField(max_length=16)     # 出勤
#     interaction = models.IntegerField(max_length=128)    # 互动次数
#     grade = models.IntegerField(max_length=128)
#     stu_id = models.ForeignKey('Student', on_delete=models.CASCADE)
#     course_time = models.IntegerField(max_length=128)    # 课次
#
#     def __str__(self):
#         return str(self.sum_id)
#
#     def condi(self):
#         return Summary.objects.filter(Q(course_id='001'))
#
#
# class Selection(models.Model):
#     stu_id = models.ForeignKey('Student', on_delete=models.CASCADE)
#     course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.stu_id)
#
#
# class Admin(models.Model):
#     admin_user = models.CharField(max_length=128, unique=True, primary_key=True)
#     admin_pwd = models.CharField(max_length=128)
#
# def con():
#     print("************************************************")
#     stu_list = Student.objects.filter(stu_id='M20180001')
#     print(stu_list)
#     return stu_list
#


# Create your models here.
# 学生信息
class Student(models.Model):
    GENDER_CHOICES = (
        (u'male', u'男'),
        (u'female', u'女'),
    )
    stu_id = models.CharField(verbose_name="学号",max_length=128, primary_key=True)
    stu_name = models.CharField(verbose_name="姓名", max_length=128)
    stu_img = models.ImageField(upload_to="img", verbose_name="照片")
    stu_sex = models.CharField(verbose_name="性别", max_length=4, choices=GENDER_CHOICES)
    stu_age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.stu_id + "(" + self.stu_name+")"


# 教师信息
class Teacher(models.Model):
    GENDER_CHOICES = (
        (u'male', u'男'),
        (u'female', u'女'),
    )
    teacher_id = models.CharField(verbose_name="工号", max_length=128, primary_key=True)
    teacher_name = models.CharField(verbose_name="姓名", max_length=128)
    teacher_pwd = models.CharField(verbose_name="密码", max_length=128)
    teacher_sex = models.CharField(verbose_name="性别", max_length=4, choices=GENDER_CHOICES)
    teacher_age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.teacher_id + "(" + self.teacher_name+")"


# 课程信息
class Course(models.Model):
    course_id = models.CharField(verbose_name="课程号", max_length=128)
    course_name = models.CharField(verbose_name="课程名", max_length=128)
    course_teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    course_total = models.IntegerField(verbose_name="总课时")

    def __str__(self):
        return self.course_id + "(" + self.course_name + ")"


# 选课信息
class CourseSelection(models.Model):
    course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    stu_id = models.ForeignKey("Student", on_delete=models.CASCADE)


# 课堂详细信息，每一条信息针对某一个学生：包括学生到课情况，加分，问答次数，该课的课程号、课次
class CourseDetail(models.Model):
    course_time = models.IntegerField(verbose_name="课次")
    course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    stu_id = models.ForeignKey("Student", on_delete=models.CASCADE)
    detail_attendance = models.BooleanField(verbose_name="到课")
    detail_answer = models.IntegerField(verbose_name="回答问题", default=0)
    detail_grade = models.IntegerField(verbose_name="加分", default=0)

    # def __str__(self):
    #     return self. + "第" + self.course_time + "次课"

