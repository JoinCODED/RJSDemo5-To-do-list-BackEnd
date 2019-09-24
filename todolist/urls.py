
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from apis.views import TaskViewSet

router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet, basename='task')

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
