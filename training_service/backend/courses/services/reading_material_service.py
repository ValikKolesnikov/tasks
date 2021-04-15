from rest_framework.generics import get_object_or_404

from courses import models
from courses.services import course_service


def set_complete(reading_material, user):
    course_progress = course_service.get_course_progress(reading_material.course, user)
    reading_material_progress = get_object_or_404(queryset=models.ReadingMaterialProgress.objects.all(),
                                                  course_progress=course_progress,
                                                  reading_material=reading_material)
    reading_material_progress.is_complete = True
    reading_material_progress.save()


def create_reading_material_progress(reading_material, user):
    course_progress = course_service.get_course_progress(reading_material.course, user)
    reading_material_progress, is_create = models.ReadingMaterialProgress.objects.get_or_create(
        course_progress=course_progress,
        reading_material=reading_material)
    if is_create:
        reading_material_progress.save()
