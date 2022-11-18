from rest_framework.generics import CreateAPIView

from apps.reservation.models import Reservation
from apps.reservation.serializers.reservation_serializer import ReservationSerializer


class CreateReservation(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
