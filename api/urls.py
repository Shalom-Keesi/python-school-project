
from django.urls import path
from .views import PeriodListViews, CourseListViews, CourseDetailView , ClassroomListViews, ClassroomDetailView , Class_PeriodDetailView , StudentListViews , TeacherListViews , StudentDetailView , TeacherDetailView , TeacherListViews

urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Courses/",CourseListViews.as_view(),name = "course_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "student_class_list_view"),
    path("Period/",PeriodListViews.as_view(),name = "class_period_list_view"),
    path("Students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
    path("Teachers/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
    path("Courses/<int:id>/", CourseDetailView.as_view(), name="course_detail_view"),
    path("Student_Class/<int:id>/", ClassroomDetailView.as_view(), name="classroom_detail_view"),
    path("Class_Period/<int:id>/", Class_PeriodDetailView.as_view(), name="class_period_detail_view")
]
