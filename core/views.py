from rest_framework import generics, viewsets
from .models import Assignment, Lecture, LectureSubject, Lecturer, Student, StudentGroup
from .serializers import AssignmentCreateSerializer, AssignmentSerializer, LectureSerializer, LectureSubjectSerializer, LecturerSerializer, StudentGroupSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse
import requests
import json


class LecturerList(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LectureViewSet(generics.ListCreateAPIView):
    serializer_class = LectureSerializer
    # filter_backends = [filters.SearchFilter]
    search_fields = ['lecturer_id']
    search_param = 'lecturer_id'
    queryset = Lecture.objects.all()

    # def get_queryset(self):
    #     lecturer_id = self.request.query_params.get('lecturer_id', None)
    #     # http://localhost:8000/api/lectures/?lecturer_id=1
    #     lectures = []
    #     if lecturer_id is not None:
    #         print(lecturer_id)
    #         lectures = Lecture.objects.filter(lecturer_id=lecturer_id)
    #         print(lectures)
    #     else:
    #         lectures = Lecture.objects.all()

    #     return lectures


class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class StudentViewSet(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGroupViewSet(generics.ListCreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


class LectureSubjectGroupViewSet(generics.ListCreateAPIView):
    queryset = LectureSubject.objects.all()
    serializer_class = LectureSubjectSerializer


class AssignmentGroupViewSet(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentGroupCreateViewSet(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentCreateSerializer


class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'success': False, 'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        student = Student.objects.filter(username=username).first()
        if student is None:
            return Response({'success': False, 'error': 'Invalid username'}, status=status.HTTP_404_NOT_FOUND)
        if not student.password == password:
            return Response({'success': False, 'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'success': True, 'student_group': student.student_group.name, 'student_number': student.username})


def send_notification(message_title, message_desc):
    fcm_api = "AAAAS-Mm1Wc:APA91bE2r9SQh-oi1vnLtKQqcX_IczSv06Q_TisEIa54vFvvhXbPlNxZ4lOr-KbYP7_Ae44decZdusULdYmZhhFSx0Zv6cutcfzEODiJwQ1av8u0TKr4xvDpjIBPhhIOUUJxQbh5Vysi"
    # url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key='+fcm_api}

    data = {
        "priority": "high",
        "title": message_title,
        "body": message_desc
    }

    notification = {
        "body": message_desc,
        "title": message_title,
    }

    data = {
        'to': 'dnpFsBiuQNGbYnIa2h6ZJe:APA91bHqRE8tclAXbYvWTt-Yx2iEfdnz5WgGNyT3WqpmxxRwOVE5yuWm8S5BEWoO4NeO4mERnexI5BZU5MX9o0UMHDVYgU0KJHJFfaKgmnZbGoLpB20W9EWe9HLPliZE2__GQ4wgMvdu',
        'data': data,
        'notification': notification
    }
    response = requests.post(
        'https://fcm.googleapis.com/fcm/send', json=data, headers=headers)
    if response.status_code == 200:
        print('FCM message sent successfully')
    else:
        print('FCM message sending failed')

    # result = requests.post(url,  data=json.dumps(payload), headers=headers)


def send(request):
    send_notification('Second Test',
                      'Second Test')
    return HttpResponse("sent")
