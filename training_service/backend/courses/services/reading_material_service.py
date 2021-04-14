from rest_framework.generics import get_object_or_404

from courses import models


def set_complete(reading_material, user):
    participation = get_object_or_404(queryset=models.Participation.objects.all(),
                                      course=reading_material.course,
                                      user=user)
    course_progress = get_object_or_404(queryset=models.CourseProgress.objects.all(),
                                        participation=participation)
    reading_material_progress = get_object_or_404(queryset=models.ReadingMaterialProgress.objects.all(),
                                                  course_progress=course_progress,
                                                  reading_material=reading_material)
    reading_material_progress.is_complete = True
    reading_material_progress.save()
