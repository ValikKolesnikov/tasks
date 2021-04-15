from rest_framework.generics import get_object_or_404

from courses import models
from courses.services import course_service


def is_answer_right(question, answers_ids):
    right_answers = models.Answer.objects.filter(question=question, is_right=True)
    right_answers_ids = [answer.id for answer in right_answers]
    return right_answers_ids == answers_ids


def set_question_done(test, user, question):
    course_progress = course_service.get_course_progress(test.course, user)
    question_progress, is_created = models.QuestionProgress.objects.get_or_create(question=question,
                                                                                  course_progress=course_progress)

    question_progress.is_done = True
    question_progress.save()


def is_all_questions_done(test, user):
    course_progress = course_service.get_course_progress(test.course, user)
    questions = models.Question.objects.filter(test=test)
    questions_progresses = models.QuestionProgress.objects.filter(question__in=questions,
                                                                  course_progress=course_progress)
    done_questions = questions_progresses.filter(is_done=True)
    return questions_progresses.count() == done_questions.count()


def set_complete(test, user):
    course_progress = course_service.get_course_progress(test.course, user)
    test_progress = get_object_or_404(queryset=models.TestProgress.objects.all(),
                                      course_progress=course_progress,
                                      test=test)
    test_progress.is_complete = True
    test_progress.save()


def create_test_progress(test, user):
    course_progress = course_service.get_course_progress(test.course, user)
    test_progress, is_created = models.TestProgress.objects.get_or_create(course_progress=course_progress,
                                                                          test=test)
    if is_created:
        test_progress.save()
