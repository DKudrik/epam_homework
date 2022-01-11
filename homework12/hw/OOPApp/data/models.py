from __future__ import annotations

from django.db import models


class DeadlineError(Exception):
    def __init__(self):
        self.text = "You are late"


class Teacher(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"Teacher {self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f"Student {self.first_name} {self.last_name}"


class HomeWork(models.Model):
    text = models.TextField()
    deadline = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="homeworks",
    )

    def __str__(self):
        return (
            f"Homework object. Text: {self.text}, deadline:{self.deadline},"
            f"created:{self.created}"
        )


class HomeworkResult(models.Model):
    author = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="homeworkresults",
    )
    homework = models.ForeignKey(
        HomeWork,
        on_delete=models.CASCADE,
        related_name="homeworkresults",
    )
    solution = models.TextField()
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"HomeworkResult instance. Solution: {self.solution}"
