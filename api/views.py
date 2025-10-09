from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers



def home(request):
    return HttpResponse("Welcome to the DRF project!")

def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializers = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type = 'application/json')

def student_list(request):
    stu = Student.objects.all()
    serializers = StudentSerializers(stu, many = True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type = 'application/json')     