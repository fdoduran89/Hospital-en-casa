from hospiApp.models.psalud import Personalsalud
from hospiApp.models.user import User
from rest_framework import serializers
from dataclasses import field

class PersonalsaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalsalud
        fields = '_all_'