from django.urls import path

from courses.views import CourseListView


urlpatterns = [
  path('', CourseListView.as_view(), name='courses_list'),
]
