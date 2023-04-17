from django.urls import path
from .views import LectureDetail, LectureViewSet, LecturerList, LecturerDetail, LoginView, StudentViewSet

urlpatterns = [
    path('lecturers/', LecturerList.as_view(), name='lecturer_list'),
    path('lecturers/<int:pk>/', LecturerDetail.as_view(), name='lecturer_detail'),
    path('lectures/',
         LectureViewSet.as_view({'get': 'list'}), name='lecturer_list'),
    path('lectures/<int:pk>/', LectureDetail.as_view(), name='lecturer_detail'),
    path('login/',
         LoginView.as_view(), name='login')
]
