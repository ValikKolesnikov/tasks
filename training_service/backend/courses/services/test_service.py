from rest_framework.generics import get_object_or_404

from courses import models


def is_answer_right(test, answers_ids):
    question = models.Question.objects.get(test=test)
    right_answers = models.Answer.objects.filter(question=question, is_right=True)
    right_answers_ids = [answer.id for answer in right_answers]
    return right_answers_ids == answers_ids


def set_complete(test, user):
    participation = get_object_or_404(queryset=models.Participation.objects.all(),
                                      course=test.course,
                                      user=user)
    course_progress = get_object_or_404(queryset=models.CourseProgress.objects.all(),
                                        participation=participation)
    test_progress = get_object_or_404(queryset=models.TestProgress.objects.all(),
                                      course_progress=course_progress,
                                      test=test)
    test_progress.is_complete = True
    test_progress.save()
