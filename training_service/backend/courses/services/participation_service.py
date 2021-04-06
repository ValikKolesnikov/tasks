from courses.models import Role


def get_participation_data(user, course, is_teacher, enroll_time=None):
    if is_teacher:
        role = Role.TEACHER
    else:
        role = Role.STUDENT
    return {
        'user': user.id,
        'course': course.id,
        'enroll_time': enroll_time,
        'role': role
    }
