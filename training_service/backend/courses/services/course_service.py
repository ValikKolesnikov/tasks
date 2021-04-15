from courses import models


def calculate_course_progress(course_progress):
    tests_complete_count = models.TestProgress.objects.filter(course_progress_id=course_progress.id,
                                                              is_complete=True).count()
    readings_complete_count = models.ReadingMaterialProgress.objects.filter(course_progress_id=course_progress.id,
                                                                            is_complete=True).count()
    all_task_count = models.Task.objects.filter(course_id=course_progress.participation.course_id).count()
    return (tests_complete_count + readings_complete_count) / all_task_count * 100


def create_course_progress(participation):
    course_progress, is_created = models.CourseProgress.objects.get_or_create(participation=participation)
    if is_created:
        course_progress.save()


def get_course_progress(course, user):
    course_progress, is_created = models.CourseProgress.objects.get_or_create(participation__user=user,
                                                                              participation__course=course)
    if is_created:
        course_progress.save()
    return course_progress
