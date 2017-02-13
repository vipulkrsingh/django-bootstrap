from .models import Task
from .models import TaskActivity
from rest_framework import serializers
from myproject.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    # owner_details = serializers.RelatedField(source='owner', read_only=True)
    owner = UserSerializer()
    assigned = UserSerializer()
    people = UserSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'

class TaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = '__all__'