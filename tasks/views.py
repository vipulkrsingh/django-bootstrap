from tasks.models import Task
from tasks.models import TaskActivity
from tasks.serializers import TaskSerializer
from tasks.serializers import TaskActivitySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import ListView

class TaskList(APIView):
    """
    List all Tasks, or create a new task.
    """
    #ANY USER
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        tasks = Task.objects.select_related().all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
