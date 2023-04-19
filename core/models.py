import datetime
from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
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


class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Lecture(models.Model):
    subject = models.CharField(max_length=100)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.CASCADE, related_name='lectures')
    venue = models.CharField(max_length=255)
    time = models.CharField(max_length=5, validators=[validate_time_format])
    day_of_week = models.CharField(
        max_length=9, choices=[(day.value, day.name) for day in Weekdays])

    def __str__(self):
        return self.subject


class StudentGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(
        max_length=255, unique=True, blank=False)
    username = models.CharField(
        max_length=255, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=255)
    student_group = models.ForeignKey(
        StudentGroup, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.username
