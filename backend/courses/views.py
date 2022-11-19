from rest_framework.generics import ListAPIView

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
