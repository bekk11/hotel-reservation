from rest_framework import serializers

from apps.service.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'info',
            'image',
            'price'
        ]
