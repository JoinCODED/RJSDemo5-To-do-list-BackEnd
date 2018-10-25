from rest_framework.generics import ListAPIView
from .models import Task
from .serializers import ListSerializer



class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ListSerializer