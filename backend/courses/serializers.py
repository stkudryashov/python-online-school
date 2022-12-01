from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course
from lessons.models import Module


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer для информации о курсе
    """

    class Meta:
        model = Course
        fields = ('id', 'title', 'description')
        read_only_fields = ('id',)


class ModuleSerializer(serializers.ModelSerializer):
    """
    Serializer для модулей курса
    """

    class Meta:
        model = Module
        fields = ('id', 'title', 'description')
        read_only_fields = ('id',)


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Serializer для подробной информации о курсе
    """

    modules = SerializerMethodField(method_name='get_order_modules_list')

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'modules')
        read_only_fields = ('id', 'modules')

    def get_order_modules_list(self, instance):
        """
        Получить отсортированный по порядку список модулей курса
        """

        mudules_list = instance.modules.order_by('coursemodule__order_number')
        return ModuleSerializer(mudules_list, many=True, read_only=True).data
