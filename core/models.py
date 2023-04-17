from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

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
