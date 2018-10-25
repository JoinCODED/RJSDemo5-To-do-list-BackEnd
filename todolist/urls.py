
from django.contrib import admin
from django.urls import path
from apis.views import TaskListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', TaskListView.as_view(), name='task-list'),
]
