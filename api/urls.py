from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, JobViewSet, HiredEmployeeViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'hired_employees', HiredEmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]