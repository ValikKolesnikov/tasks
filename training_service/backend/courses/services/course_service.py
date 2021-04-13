from django.db.models import Func, F, Subquery, Count, OuterRef

from courses.models import Task, CourseProgress, TestProgress, ReadingMaterialProgress, Test, ReadingMaterial
from courses.serializers import TestResponseSerializer


def extract_data_from_participation(participation):
    course = participation.course
    tasks = Task.objects.filter(course__id=course.id)
    test_progress = TestProgress.objects.filter(course_progress__participation_id=participation.id,
                                                test_id=OuterRef('pk'))
    reading_material_progress = ReadingMaterialProgress.objects.filter(
        course_progress__participation_id=participation.id,
        reading_material_id=OuterRef('pk')
    )
    tests = tasks.instance_of(Test).annotate(is_complete=Subquery(test_progress.values('is_complete')))
    reading_materials = tasks.instance_of(ReadingMaterial).annotate(
        is_complete=Subquery(reading_material_progress.values('is_complete')))
    tasks = tests | reading_materials
    course.progress = CourseProgress.objects.get(participation__id=participation.id)
    return {
        'tasks': tasks,
        'course': course
    }
