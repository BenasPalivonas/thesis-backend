from django.db import models


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
