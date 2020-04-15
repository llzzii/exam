from django.db import models

# Create your models here.


class Exam(models.Model):
    # username，password 表示创建字段名，长度为32

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    keys = models.CharField(max_length=255)
    a_key = models.CharField(max_length=255)
    b_key = models.CharField(max_length=255)
    c_key = models.CharField(max_length=255)
    d_key = models.CharField(max_length=255)
    answer = models.CharField(max_length=5000)
    resolve = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class ExamType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
