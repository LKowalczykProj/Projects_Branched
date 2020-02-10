from .models import Actor
from .serializers import ActorSerializer
from rest_framework import viewsets


class ActorViewSet(viewsets.ModelViewSet):

    serializer_class = ActorSerializer

    def get_queryset(self):
        query = Actor.objects.all()
        return query
