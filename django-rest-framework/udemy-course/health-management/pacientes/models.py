from django.db import models


class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(
        max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateField(auto_now_add=True)
    rg = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pacientes'
