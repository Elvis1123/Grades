from django.shortcuts import render
from rest_framework import viewsets
from . models import Subject,Grade,Student
from . serializers import SubjectSerializer,GradeSerializer,StudentSerializer

class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class GradeView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
