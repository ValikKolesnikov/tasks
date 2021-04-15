from rest_framework.generics import get_object_or_404

from courses import models


def get_course_progress(test, user):
    participation = get_object_or_404(queryset=models.Participation.objects.all(),
                                      course=test.course,
                                      user=user)
    course_progress = get_object_or_404(queryset=models.CourseProgress.objects.all(),
                                        participation=participation)
    return course_progress


def is_answer_right(test, answers_ids):
    question = get_object_or_404(queryset=models.Question.objects.all(), test=test)
    right_answers = models.Answer.objects.filter(question=question, is_right=True)
    right_answers_ids = [answer.id for answer in right_answers]
    return right_answers_ids == answers_ids


def set_answer_done(test):
    question = get_object_or_404(queryset=models.Question.objects.all(), test=test)
    question.is_done = True
    question.save()


def set_complete(test, user):
    course_progress = get_course_progress(test=test,
                                          user=user)
    test_progress = get_object_or_404(queryset=models.TestProgress.objects.all(),
                                      course_progress=course_progress,
                                      test=test)
    test_progress.is_complete = True
    test_progress.save()


def create_test_progress(test, user):
    course_progress = get_course_progress(test=test,
                                          user=user)
    test_progress = models.TestProgress(course_progress=course_progress,
                                        test=test)
    test_progress.save()
    return test_progress
