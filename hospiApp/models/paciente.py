from django.db import models
from user import User 
from psalud import id_personalSalud 
class pacientes (models.Model)
    id_paciente = models.BigAutoField(primary_key=True)
    personasalud = models.ForeignKey(id_personalSalud, related_name='ID P_SALUD', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='Usuario', on_delete=models.CASCADE)
    city = models.CharField('Ciudad', max_length=15)
    birthday = models.DateField('Fecha de Nacimiento')  