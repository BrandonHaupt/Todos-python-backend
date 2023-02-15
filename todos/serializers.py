from .models import Todo
from rest_framework import serializers

# Our TodoSerializer
# Serializing objects into json strings and then turning them back into python dictionaries can be a tedious process. 
# With djangorestframework, we can build a serializer for our model that handles all this for us along with arranging the data in a more traditional form.
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Todo
        # the fields that should be included in the serialized output
        # Subject an Details were created in our models.py file
        fields = ['id', 'subject', 'details']