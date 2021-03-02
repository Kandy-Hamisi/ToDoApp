from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


# Specifies the model to work with and the fields to be converte
# to JSON