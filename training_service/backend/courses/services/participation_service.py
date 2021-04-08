from courses.models import Role, Participation


def enroll_as_student(user, course):
    return Participation(user=user, course=course, role=Role.STUDENT)


def enroll_as_teacher(user, course):
    return Participation(user=user, course=course, role=Role.TEACHER)


