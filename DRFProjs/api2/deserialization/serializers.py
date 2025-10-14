from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    classs = serializers.IntegerField()
    section = serializers.CharField(max_length=1)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)