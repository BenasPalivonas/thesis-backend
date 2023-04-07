from rest_framework import serializers
from .models import StudentGroup, Lecture, Lecturer, Student


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'email']


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'subject', 'lecturer']


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'username',
                  'email', 'student_group', 'password']

    def create(self, validated_data):
        name = validated_data.pop('username')
        password = validated_data.pop('password')
        student = Student(**validated_data)
        student.set_password(password)
        student.save()
        return student


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['id', 'group_name']
