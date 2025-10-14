from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt

def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'created entry'}
            return JsonResponse(response, safe=False)
        return JsonResponse(serializer.errors)