from django.urls import path
from .views import LecturerList, LecturerDetail

urlpatterns = [
    path('lecturers/', LecturerList.as_view(), name='lecturer_list'),
    path('lecturers/<int:pk>/', LecturerDetail.as_view(), name='lecturer_detail'),
]
