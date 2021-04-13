from courses.models import Task


def extract_data_from_participation(participation):
    course = participation.course
    tasks = Task.objects.filter(course__id=course.id)
    return {
        'tasks': tasks,
        'course': course
    }
