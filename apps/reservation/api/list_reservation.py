from rest_framework.generics import ListAPIView

from apps.reservation.models import Reservation
from apps.reservation.serializers.reservation_serializer import ReservationSerializer


class ListReservation(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
