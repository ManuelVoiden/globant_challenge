from django.shortcuts import render

from rest_framework import viewsets
from .models import Department, Job, HiredEmployee
from .serializers import DepartmentSerializer, JobSerializer, HiredEmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class HiredEmployeeViewSet(viewsets.ModelViewSet):
    queryset = HiredEmployee.objects.all()
    serializer_class = HiredEmployeeSerializer
