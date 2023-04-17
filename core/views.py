from rest_framework import generics, viewsets, filters
from .models import Lecture, Lecturer, Student, StudentGroup
from .serializers import LectureSerializer, LecturerSerializer, StudentGroupSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.decorators import api_view


class LecturerList(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LecturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['lecturer_id']
    search_param = 'lecturer_id'

    def get_queryset(self):
        queryset = self.queryset
        lecturer_id = self.request.query_params.get('lecturer_id', None)
        # http://localhost:8000/api/lectures/?lecturer_id=1

        if lecturer_id is not None:
            queryset = queryset.filter(lecturer_id=lecturer_id)

        return queryset


class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer


@api_view(['POST'])
def login(request):
    if request.method == "POST":
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
