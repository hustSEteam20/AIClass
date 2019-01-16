from django.shortcuts import render
from django.template import RequestContext
from server import models
# Create your views here.


def index(request):

    return render(request, 'index.html')

def list(request):
    user_list = []
    if request.method == 'POST':
        id = request.POST.get('stu_id')
        name = request.POST.get('stu_name')
        sex = request.POST.get('stu_sex')
        age = request.POST.get('stu_age')
        print(id, name)
        models.Student.objects.create(stu_id=id, stu_name=name, stu_sex=sex, stu_age=age)
    user_list = models.Student.objects.all()
    return render(request, 'server_temp/tables.html', {'data': user_list})


