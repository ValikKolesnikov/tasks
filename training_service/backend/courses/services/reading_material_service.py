from rest_framework.generics import get_object_or_404

from courses import models


def get_course_progress(reading_material, user):
    participation = get_object_or_404(queryset=models.Participation.objects.all(),
                                      course=reading_material.course,
                                      user=user)
    course_progress = get_object_or_404(queryset=models.CourseProgress.objects.all(),
                                        participation=participation)
    return course_progress


def set_complete(reading_material, user):
    course_progress = get_course_progress(reading_material=reading_material,
                                          user=user)
    reading_material_progress = get_object_or_404(queryset=models.ReadingMaterialProgress.objects.all(),
                                                  course_progress=course_progress,
                                                  reading_material=reading_material)
    reading_material_progress.is_complete = True
    reading_material_progress.save()


def create_reading_material_progress(reading_material, user):
    course_progress = get_course_progress(reading_material=reading_material,
                                          user=user)
    reading_material_progress = models.ReadingMaterialProgress(course_progress=course_progress,
                                                               reading_material=reading_material)
    reading_material_progress.save()
    return reading_material_progress
