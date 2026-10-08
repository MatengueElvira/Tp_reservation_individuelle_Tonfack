"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from datetime import timedelta

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Reservation, Salle
from .permissions import IsOwnerOrReadOnly
from .serializers import ReservationSerializer, SalleSerializer

class SalleViewsSet (viewsets.ModelViewSet):
    queryset =Salle.objects.all()
    serializer_class = SalleSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    @action(detail=True, methods=["get"])
    def occupation(self, request, pk=None):
        salle = self.get_object()
        debut = lire_datetime("debut", request.query_params.get("debut"))
        fin = lire_datetime("fin", request.query_params.get("fin"))
        if fin <= debut:
            raise ValidationError({"fin": "La fin doit être strictement inferieur  au début."})

        reservations = Reservation.objects.filter(
            salle=salle,
            statut="CONFIRMEE",
            fin__gt=debut,
        )
        duree_reservee = sum(
            (min(r.fin, fin) - max(r.debut, debut) for r in reservations),
            timedelta(),
        )
        taux = min(duree_reservee / (fin - debut), 1.0)

        return Response({
            "salle": salle.id,
            "debut": debut,
            "fin": fin,
            "heures_reservees": duree_reservee.total_seconds(),
            "taux_occupation": round(taux, 4),
        })


    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)



