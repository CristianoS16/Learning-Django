# Generated by Django 4.1.1 on 2022-09-10 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id_agendamento', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('cancelado', models.BooleanField(default=False)),
                ('observacao', models.TextField()),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='pacientes.pacientes')),
            ],
            options={
                'db_table': 'agendamentos',
                'managed': True,
                'unique_together': {('data_hora', 'id_paciente')},
            },
        ),
    ]
