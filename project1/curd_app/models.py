from django.db import models


class SchoolTeacher(models.Model):
    teacher_school_name = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=20)
    school_location = models.CharField(max_length=20)
    teaching_experience = models.IntegerField()
    teacher_age = models.IntegerField()
    teacher_address = models.CharField(max_length=30)

