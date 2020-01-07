from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subjects',views.SubjectView)
router.register('grades',views.GradeView)
router.register('students',views.StudentView)

urlpatterns = [

    path('', include(router.urls))

]
