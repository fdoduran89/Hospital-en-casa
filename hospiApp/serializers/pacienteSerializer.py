from hospiApp.models.paciente import Pacientes
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = ['id_paciente','id_psalud','username','city','birthday']
