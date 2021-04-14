from courses import models


def calculate_course_progress(course_progress):
    tests_complete_count = models.TestProgress.objects.filter(course_progress_id=course_progress.id,
                                                              is_complete=True).count()
    readings_complete_count = models.ReadingMaterialProgress.objects.filter(course_progress_id=course_progress.id,
                                                                            is_complete=True).count()
    all_task_count = models.Task.objects.filter(course_id=course_progress.participation.course_id).count()
    return (tests_complete_count + readings_complete_count) / all_task_count * 100
