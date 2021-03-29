from django.db import models
from django.contrib.auth.models import User, Group, Permission


# Create your models here.
class Role(models.TextChoices):
    TEACHER = 'TH', 'Teacher'
    STUDENT = 'ST', 'Student'


class Course(models.Model):
    name = models.CharField('Name', max_length=300)
    description = models.TextField('Description')
    users = models.ManyToManyField('User', through='Participation')


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_time = models.DateTimeField('Enroll date')
    role = models.CharField('Role', max_length=2, choices=Role.choices, default=Role.STUDENT)


class CourseProgress(models.Model):
    completion_date = models.DateField('Completion date')
    is_complete = models.BooleanField('Is complete')
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)


class ReadingMaterial(models.Model):
    title = models.CharField('Title', max_length=300)
    text = models.TextField('Text')
    position_number = models.IntegerField('Position number')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Test(models.Model):
    name = models.CharField('Name', max_length=100)
    position_number = models.IntegerField('Position number')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.CharField('Text', max_length=500)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    text = models.CharField('Text', max_length=500)
    is_right = models.BooleanField('Is right')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class ReadingMaterialProgress(models.Model):
    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)


class TestProgress(models.Model):
    reading_material = models.ForeignKey(ReadingMaterial, on_delete=models.CASCADE)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)
