from rest_framework import serializers

from apps.room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'category',
            'name',
            'info',
            'image1',
            'image2',
            'image3',
            'image4',
            'floor',
            'room_number',
            'bedroom',
            'hall',
            'bathroom',
            'single_beds',
            'double_beds',
            'air_conditioner',
            'kitchen',
            'hair_dryer',
            'iron',
            'wifi',
            'TV',
            'price',
            'busy',
        ]
