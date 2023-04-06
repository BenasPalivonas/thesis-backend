from rest_framework import generics, viewsets, filters
from .models import Lecture, Lecturer
from .serializers import LectureSerializer, LecturerSerializer


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
