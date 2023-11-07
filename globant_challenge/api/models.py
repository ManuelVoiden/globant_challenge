from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=100)

class Job(models.Model):
    job = models.CharField(max_length=100)

class HiredEmployee(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)