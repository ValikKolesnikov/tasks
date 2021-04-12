from courses.models import TaskProgress, Task, CourseProgress


def get_course_data(participation):
    tasks = Task.objects.filter(course__id=participation.course.id)
    tasks_progresses = TaskProgress.objects.filter(task__in=tasks)
    tasks_id = tasks_progresses.values_list('task_id', flat=True)
    for task in tasks:
        task.is_complete = task.id in tasks_id
    return {
        'tasks': tasks,
        'course': participation.course,
        'course_progress': CourseProgress.objects.get(participation__id=participation.id)
    }
