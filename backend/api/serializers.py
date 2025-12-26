"""imports."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """serializer."""

    class Meta:
        """meta serializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
