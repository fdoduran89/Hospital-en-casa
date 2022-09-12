from hospiApp.models.psalud import Personalsalud
from hospiApp.models.user import User
from rest_framework import serializers


class PersonalsaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud
        fields = ['id_psalud', 'username', 'rol', 'especialidad']
