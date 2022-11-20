from django.urls import path

from courses.views import CourseListView, CourseRetrieveView


urlpatterns = [
  path('', CourseListView.as_view(), name='courses_list'),
  path('<int:pk>/', CourseRetrieveView.as_view(), name='courses_retrieve')
]
