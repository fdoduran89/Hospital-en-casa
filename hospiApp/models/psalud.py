from django.db import models
from user import User
from paciente import Pacientes

class Personalsalud (models.Model):
    ip_psalud = models.AutoField (primary_key=True)
    username = models.ForeignKey(User, related_name='psalud', on_delete=models.CASCADE)
    rol=models.CharField('Rol',max_length=35)
    especialidad=models.CharField('Especialidad',max_length=35)