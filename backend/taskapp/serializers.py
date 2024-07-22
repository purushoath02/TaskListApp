from rest_framework import serializers

# import the todo data model
from .models import Task

# create a serializer class
class TaskSerializer(serializers.ModelSerializer):

    # create a meta class
    class Meta:
        model = Task
        fields = ('id', 'title','description','completed')
