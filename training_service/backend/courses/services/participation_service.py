from courses.models import Role, Participation
from courses.serializers import ParticipationRequestSerializer


def enroll_as_student(user, course):
    participation_data = {
        'user': user,
        'course': course,
        'enroll_time': None,
        'role': Role.STUDENT
    }
    return enroll(participation_data)


def enroll_as_teacher(user, course):
    participation_data = {
        'user': user,
        'course': course,
        'enroll_time': None,
        'role': Role.TEACHER
    }
    enroll(participation_data)


def enroll(data):
    participation_serializer = ParticipationRequestSerializer(data=data)
    participation_serializer.is_valid(raise_exception=True)
    participation = participation_serializer.save()
    return participation
