from django.urls import path
from .views import AssignmentDetail, AssignmentGroupCreateViewSet, AssignmentGroupViewSet, LectureDetail, LectureSubjectGroupViewSet, LectureViewSet, LecturerList, LecturerDetail, LoginView, StudentViewSet, send

urlpatterns = [
    path('lecturers/', LecturerList.as_view(), name='lecturer_list'),
    path('lecturers/<int:pk>/', LecturerDetail.as_view(), name='lecturer_detail'),
    path('lectures/',
         LectureViewSet.as_view(), name='lectures_list'),
    path('lectures/<int:pk>/', LectureDetail.as_view(), name='lectures_list'),
    path('assignments/',
         AssignmentGroupViewSet.as_view(), name='assigments_list'),
    path('assignments/create',
         AssignmentGroupCreateViewSet.as_view(), name='assigments_list'),
    path('assignments/<int:pk>/', AssignmentDetail.as_view(),
         name='assigments_list'),
    path('lecture_subjects/',
         LectureSubjectGroupViewSet.as_view(), name='assigments_list'),
    path('lecture_subjects/<int:pk>/', LectureSubjectGroupViewSet.as_view(),
         name='assigments_list'),

    path('login/',
         LoginView.as_view(), name='login')
]
