"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets
# noqa: F401  (a utiliser)

from  .serializers import SalleSerializer,ReservationSerializer



from .models import Reservation, Salle  # noqa: F401  (a utiliser)

class SalleViewsSet (viewsets.ModelViewSet):
    queryset =Salle.objects.all()
    serializer_class = SalleSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    # def perform_create(self, serializer):
    #     serializer.save(utilisateur=self.request.user)



