from rest_framework import serializers
from .models import StudentGroup, Lecture, Lecturer, Student
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters import rest_framework as filters


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'email']


class LectureSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()

    class Meta:
        model = Lecture
        fields = ['id', 'subject', 'lecturer', 'time', 'day_of_week', 'venue']


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'username',
                  'email', 'student_group', 'password']


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['id', 'group_name']


class LoginInfo:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
