from django.forms import model_to_dict
from rest_framework import generics, viewsets
from .models import Assignment, Venue, Lecture, LectureSubject, Lecturer, Student, StudentGroup
from .serializers import AssignmentCreateSerializer, AssignmentSerializer, LectureSerializer, LectureSubjectSerializer, LecturerSerializer, StudentGroupSerializer, StudentSerializer, VenueSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse
import requests
import json
from django.core import serializers

from core import models


class LecturerList(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LectureViewSet(generics.ListCreateAPIView):
    serializer_class = LectureSerializer
    search_fields = ['lecturer_id']
    search_param = 'lecturer_id'
    queryset = Lecture.objects.all()


class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class StudentViewSet(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class VenueViewSet(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


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
        return Response({'success': True, 'id': student.id, 'student_group': student.student_group.name, 'student_number': student.username})


def send_notification(instance, created, is_grade, assignment_id):
    fcm_api = "AAAAS-Mm1Wc:APA91bE2r9SQh-oi1vnLtKQqcX_IczSv06Q_TisEIa54vFvvhXbPlNxZ4lOr-KbYP7_Ae44decZdusULdYmZhhFSx0Zv6cutcfzEODiJwQ1av8u0TKr4xvDpjIBPhhIOUUJxQbh5Vysi"
    # url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key='+fcm_api}

    body = ''
    if (is_grade):
        body = instance.assignment.name
    else:
        body = instance.name

    data = {
        "priority": "high",
        "id": assignment_id,
    }
    title = ""

    if (created):
        if (is_grade):
            title = "New grade for your assignment"
        else:
            title = "New assignment"
    else:
        if (is_grade):
            title = "Your grade for an assignment was updated"
        else:
            title = "Your Assignment was updated"

    notification = {
        "title": title,
        "body": body,
    }
    print(is_grade)
    data = {
        'to': 'dnpFsBiuQNGbYnIa2h6ZJe:APA91bHqRE8tclAXbYvWTt-Yx2iEfdnz5WgGNyT3WqpmxxRwOVE5yuWm8S5BEWoO4NeO4mERnexI5BZU5MX9o0UMHDVYgU0KJHJFfaKgmnZbGoLpB20W9EWe9HLPliZE2__GQ4wgMvdu',
        'data': data,
        'notification': notification,
        'is_grade': is_grade
    }
    response = requests.post(
        'https://fcm.googleapis.com/fcm/send', json=data, headers=headers)
    print('SENDING')
    if response.status_code == 200:
        print('FCM message sent successfully')
    else:
        print('FCM message sending failed')

    # result = requests.post(url,  data=json.dumps(payload), headers=headers)


def schedule_fcm_message(message_title, message_body, scheduled_time):
    # Create a ScheduledMessage instance
    scheduled_message = ScheduledMessage.objects.create(
        message_title=message_title,
        message_body=message_body,
        scheduled_time=scheduled_time
    )

    # Get the UTC timestamp of the scheduled time
    utc_scheduled_time = timezone.localtime(
        scheduled_time).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # Get the registration IDs of the devices to send the message to
    registration_ids = ["registration_id_1", "registration_id_2"]

    # Schedule the FCM message using the Firebase Cloud Messaging API
    send_at = {"sendAt": utc_scheduled_time}
    payload = {"message": {"notification": {
        "title": message_title, "body": message_body}}, "schedule": send_at}
    response = send_fcm_message(registration_ids, payload)

    # Update the ScheduledMessage instance with the FCM message ID and status
    scheduled_message.fcm_message_id = response.json()['name']
    scheduled_message.status = ScheduledMessage.SENT
    scheduled_message.save()

# model for scheduled messages
# class ScheduledMessage(models.Model):
#     SENT = 'SENT'
#     PENDING = 'PENDING'
#     STATUS_CHOICES = [
#         (SENT, 'Sent'),
#         (PENDING, 'Pending'),
#     ]

#     message_title = models.CharField(max_length=255)
#     message_body = models.TextField()
#     scheduled_time = models.DateTimeField()
#     fcm_message_id = models.CharField(max_length=255, null=True, blank=True)
#     status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=PENDING)


def send(request):
    send_notification('Second Test',
                      'Second Test')
    return HttpResponse("sent")
