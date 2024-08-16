from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField()

    def ger_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    amount_of_lessons_in_course = SerializerMethodField()

    def get_amount_of_lessons_in_course(self, lesson):
        return Lesson.objects.filter.count(course=lesson.course)

    class Meta:
        model = Lesson
        fields = ('name', 'course', 'get_amount_of_lessons_in_course')


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
