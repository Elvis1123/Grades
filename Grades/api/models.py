from django.db import models

class Grade(models.Model):
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.grade

class Subject(models.Model):
    name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name



