from django.db import models
from django.db.models import Q
# Create your models here.


class Student(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    stu_id = models.CharField(max_length=128, unique=True, primary_key=True)
    stu_name = models.CharField(max_length=128)
    stu_photo = models.ImageField(upload_to='media',null=True)
    stu_sex = models.CharField(max_length=32, choices=gender, default='男')
    stu_age = models.IntegerField(null=True)

    def __str__(self):
        return str(self.stu_id)

    def condition(self):
        if self.stu_id == 'M20180001':
            return 'yes'
        # 照片路径


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=128, unique=True, primary_key=True)
    teacher_name = models.CharField(max_length=128)
    teacher_pwd = models.CharField(max_length=128)


class Course(models.Model):
    course_id = models.CharField(max_length=128, unique=True, primary_key=True)
    course_name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.course_id)



class Summary(models.Model):
    sum_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    attendance = models.IntegerField(max_length=16)     # 出勤
    interaction = models.IntegerField(max_length=128)    # 互动次数
    grade = models.IntegerField(max_length=128)
    stu_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_time = models.IntegerField(max_length=128)    # 课次

    def __str__(self):
        return str(self.sum_id)

    def condi(self):
        return Summary.objects.filter(Q(course_id='001'))


class Selection(models.Model):
    stu_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stu_id)


class Admin(models.Model):
    admin_user = models.CharField(max_length=128, unique=True, primary_key=True)
    admin_pwd = models.CharField(max_length=128)

def con():
    print("************************************************")
    stu_list = Student.objects.filter(stu_id='M20180001')
    print(stu_list)
    return stu_list


