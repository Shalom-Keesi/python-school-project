from django.db import models

# Create your models here.
from django.db import models
from classroom.models import Classroom
from teacher.models import Teacher

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    syllabus = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    prerequisites = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trimester = models.PositiveSmallIntegerField()
    course_head = models.CharField(max_length=100)
    enrollment_limit = models.IntegerField()
    classes = models.ManyToManyField(Classroom, related_name='courses')
    def __str__(self):
        return self.name