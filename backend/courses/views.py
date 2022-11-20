from rest_framework.generics import ListAPIView, RetrieveAPIView

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
