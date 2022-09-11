from hospiApp.models.user import Pacientes
from rest_framework import serializers
from dataclasses import field

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '_all_'