from rest_framework import viewsets
from .models import Thread
from .serializers import ThreadSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

