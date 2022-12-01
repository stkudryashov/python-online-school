from rest_framework.generics import ListAPIView, RetrieveAPIView

from courses.models import Course
from courses.serializers import CourseSerializer, CourseDetailSerializer


class CourseListView(ListAPIView):
    """
    Получение списка курсов
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveView(RetrieveAPIView):
    """
    Подробная информация о курсе
    """

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
