import datetime
from django import forms
from django.db import models
from enum import Enum


class Weekdays(Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'


def validate_time_format(value):
    try:
        # Attempt to parse the time value using strptime
        time_format = '%H:%M'
        datetime.datetime.strptime(value, time_format)
    except ValueError:
        # Raise a validation error if the time value is not in the expected format
        raise forms.ValidationError('Invalid time format (expected HH:MM)')

# add max length to all


class StudentGroup(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(
        max_length=255, unique=True, blank=False, null=False)
    username = models.CharField(
        max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    student_group = models.ForeignKey(
        StudentGroup, on_delete=models.CASCADE, related_name='student', null=False, blank=False)

    def __str__(self):
        return self.username


class LectureSubject(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    def get_assignments(self):
        return Assignment.objects.filter(lecturer=self)

    def get_lectures(self):
        return Lecture.objects.filter(lecturer=self)


class Venue(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    subject = models.ForeignKey(
        LectureSubject, on_delete=models.CASCADE, related_name='lectures', null=False)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.CASCADE, related_name='lectures', null=False)
    student_groups = models.ManyToManyField(
        StudentGroup, blank=False)
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='lectures', null=False)
    time = models.CharField(max_length=5, validators=[
                            validate_time_format], blank=False, null=False)
    day_of_week = models.CharField(
        max_length=9, choices=[(day.value, day.name) for day in Weekdays], blank=False, null=False)

    def __str__(self):
        return self.subject.name


class Assignment(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    subject = models.ForeignKey(
        LectureSubject, on_delete=models.CASCADE, related_name='assignments', null=False, blank=False)
    due_date = models.DateTimeField(blank=False, null=False)
    details = models.TextField(blank=False, null=False)
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    completed = models.BooleanField(default=False, null=False)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    student_groups = models.ManyToManyField(
        StudentGroup, blank=False)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        # if self.created_by_lecturer and self.created_by_student:
        #     raise forms.ValidationError(
        #         'An assignment cannot be created by both a lecturer and a student.')
