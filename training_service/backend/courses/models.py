from django.contrib.auth.models import User, Group, Permission
from django.db import models
from polymorphic.models import PolymorphicModel

from courses.services import course_service


class Role(models.TextChoices):
    TEACHER = 'TH', 'Teacher'
    STUDENT = 'ST', 'Student'


class Course(models.Model):
    name = models.CharField('Name', max_length=300)
    description = models.TextField('Description')
    users = models.ManyToManyField(User, through='Participation')

    def __str__(self):
        return self.name


class Task(PolymorphicModel):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'position_number'], name='positioning')
        ]

    position_number = models.IntegerField('Position number')
    course = models.ForeignKey(Course, related_name='tasks', default=None, on_delete=models.CASCADE)


class Participation(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'user'], name='participation_constraint')
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_time = models.DateTimeField('Enroll date', auto_now_add=True)
    role = models.CharField('Role', max_length=2, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return f'{self.user} - {self.course}'


class CourseProgress(models.Model):
    completion_date = models.DateField('Completion date', blank=True, null=True)
    participation = models.OneToOneField(Participation, on_delete=models.CASCADE)

    def get_progress(self):
        return course_service.get_progress(self)

    def is_complete(self):
        return self.get_progress() == 100

    def __str__(self):
        return f'{self.participation.course} - {self.participation.user}'


class ReadingMaterial(Task):
    title = models.CharField('Title', max_length=300)
    text = models.TextField('Text')

    def __str__(self):
        return f'{self.course.name} - {self.title}'


class Test(Task):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return f'{self.course.name} - {self.name}'


class Question(models.Model):
    text = models.CharField('Text', max_length=500)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test.name} - {self.text}'


class Answer(models.Model):
    text = models.CharField('Text', max_length=500)
    is_right = models.BooleanField('Is right')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.text} - {self.text}'


class ReadingMaterialProgress(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['reading_material', 'course_progress'], name='reading_material_progress')
        ]

    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)
    is_complete = models.BooleanField()

    def __str__(self):
        return f'{self.reading_material} - {self.course_progress}'


class TestProgress(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['test', 'course_progress'], name='test_progress')
        ]

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)
    is_complete = models.BooleanField()

    def __str__(self):
        return f'{self.test} - {self.course_progress}'
