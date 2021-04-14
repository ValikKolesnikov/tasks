from courses import models
from courses.services import course_service


def get_reading_material_progress_or_none(reading_material_id, participation_id):
    progress = models.ReadingMaterialProgress.objects.filter(
        course_progress__participation_id=participation_id,
        reading_material_id=reading_material_id).first()
    return progress


def get_test_progress_or_none(test_id, participation_id):
    progress = models.TestProgress.objects.filter(
        course_progress__participation_id=participation_id,
        test_id=test_id).first()
    return progress


def get_course_progress_or_none(participation_id):
    progress = models.CourseProgress.objects.filter(
        participation_id=participation_id).first()
    progress_value = course_service.calculate_course_progress(progress)
    return {
        'progress': progress,
        'value': progress_value
    }
