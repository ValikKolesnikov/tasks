from courses.models import Role, Participation


def enroll_as_student(user, course):
    participation = Participation(user=user, course=course, role=Role.STUDENT)
    participation.save()
    return participation



