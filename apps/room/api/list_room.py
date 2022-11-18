import django_filters
from rest_framework.generics import ListAPIView
from rest_framework import filters

from apps.room.models import Room
from apps.room.serilaizers.room_serializer import RoomSerializer


class ListRoom(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_fields = (
        'category',
        'type_room',
        'floor',
        'air_conditioner',
        'kitchen',
        'hair_dryer',
        'iron',
        'wifi',
        'TV',
        'busy',
    )
