from django.db import models

# Create your models here.


class Intake(models.Model):
    intake_name = models.CharField(max_length=30)

    def __str__(self):
        return self.intake_name


class Track(models.Model):
    track_name = models.CharField(max_length=30)

    def __str__(self):
        return self.track_name


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_intake = models.ForeignKey(Intake, on_delete=models.CASCADE)
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name

