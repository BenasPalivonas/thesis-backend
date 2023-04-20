from rest_framework import generics, viewsets
from .models import Assignment, Lecture, LectureSubject, Lecturer, Student, StudentGroup
from .serializers import AssignmentCreateSerializer, AssignmentSerializer, LectureSerializer, LectureSubjectSerializer, LecturerSerializer, StudentGroupSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


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
        return Response({'success': True})
