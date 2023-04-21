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


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ['id', 'name']


class LectureSerializer(serializers.ModelSerializer):
    lecturer = LecturerSerializer()
    subject = LectureSubjectSerializer()
    student_groups = StudentGroupSerializer(many=True)

    class Meta:
        model = Lecture
        fields = ['id', 'subject', 'lecturer', 'time',
                  'day_of_week', 'venue', 'student_groups']


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'username',
                  'email', 'student_group', 'password']


class AssignmentSerializer(serializers.ModelSerializer):
    subject = LectureSubjectSerializer()
    lecturer = LecturerSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentCreateSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=LectureSubject.objects.all(),
        source='subject',
        write_only=True
    )

    class Meta:
        model = Assignment
        fields = ['name', 'due_date', 'details',
                  'completed', 'subject_id']
