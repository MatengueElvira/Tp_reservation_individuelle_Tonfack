"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle
class SalleSerializer(serializers.ModelSerializer):
    class meta:
        model =fields = [ 'nom', 'capacite', 'batiment']

class ReservationSerializer(serializers.ModelSerializer):

        utilisateur = serializers.StringRelatedField(read_only=True)

        class Meta:
            model = Reservation
            fields = [

                'salle',
                'utilisateur',
                'debut',
                'fin',
                'motif',
                'statut',
                'cree_le'
            ]


            def validate(self, data):

                if data.get('debut') and data.get('fin'):
                    if data['debut'] >= data['fin']:
                        raise serializers.ValidationError(
                            {"fin": "la date de fin doit être before la date de début."}
                        )
                    return data

                if statut == 'CONFIRMEE' and  salle and debut and fin:
                    chevauchement_de_date = Reservation.objects.filter(
                        salle=salle,
                        statut='CONFIRMEE',
                        debut__lt=fin,# lt plus petit qur
                        fin__gt=debut # greqtter than
                    )
                    if instance:
                        chevauchement_de_date = chevauchement_de_date.exclude(id=instance.id)

                    if chevauchement_de_date.exists():
                        raise serializers.ValidationError(
                            "Cette salle est sur tout deja reserv ."
                        )

                    return data

















