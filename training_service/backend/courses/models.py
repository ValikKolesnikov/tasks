from django.db import models
from django.contrib.auth.models import User, Group, Permission
from courses.enumerations import ROLES


# Create your models here.

class Course(models.Model):
    name = models.CharField('Name', max_length=300)
    description = models.TextField('Description')


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completion_date = models.DateField('Completion date')
    is_complete = models.BooleanField('Is complete')


class Partition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_time = models.DateTimeField('Enroll date')
    role = models.CharField('Role', max_length=2, choices=ROLES)


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