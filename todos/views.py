from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer

# djangorestframework has classes for building out views called ViewSets. With these we can wire up all our CRUD routes pretty easily.
class TodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Todo.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]