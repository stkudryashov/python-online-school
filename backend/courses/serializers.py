from rest_framework import serializers

from courses.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description')
        read_only_fields = ('id',)
