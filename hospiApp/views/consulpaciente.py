from django.conf import settings
from rest_framework import generics, status
from hospiApp.models.paciente import Pacientes
from hospiApp.serializers.pacienteSerializer import PacienteSerializer
from rest_framework.response import Response

class ConsulPaciente(generics.ListAPIView):
    serializer_class = PacienteSerializer

    def get(self,request, pk, format=None):
        modelo = Pacientes.objects.get(pk=pk)
        serializer = PacienteSerializer(modelo)
        return Response(serializer.data)

    '''def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Pacientes.objects.all()
        id_paciente = self.request.query_params.get('id_paciente')
        if id_paciente is not None:
            queryset = queryset.filter(paciente__id_paciente="1")
        return queryset'''