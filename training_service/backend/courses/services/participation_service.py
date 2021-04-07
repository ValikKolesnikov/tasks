from courses.models import Role


def enroll_as_student(user, course):
    return {
        'user': user.id,
        'course': course.id,
        'enroll_time': None,
        'role': Role.STUDENT
    }


def enroll_as_teacher(user, course):
    return {
        'user': user.id,
        'course': course.id,
        'enroll_time': None,
        'role': Role.TEACHER
    }
