from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    standard = serializers.CharField(max_length = 100)
    section = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()