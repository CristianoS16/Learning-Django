# Generated by Django 4.1.1 on 2022-09-11 19:24

from django.db import migrations, models
import pacientes.models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='selfie',
            field=models.ImageField(blank=True, null=True, upload_to=pacientes.models.imagens_selfie),
        ),
    ]