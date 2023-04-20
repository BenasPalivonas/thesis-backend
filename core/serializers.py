from rest_framework import serializers
from .models import Assignment, LectureSubject, StudentGroup, Lecture, Lecturer, Student


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'name', 'email']


class LectureSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureSubject
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()
    subject = LectureSubjectSerializer()

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


class AssignmentSerializer(serializers.ModelSerializer):
    subject = LectureSubjectSerializer()
    lecturer = LecturerSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'
