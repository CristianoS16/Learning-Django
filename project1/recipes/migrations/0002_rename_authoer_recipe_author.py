# Generated by Django 4.1 on 2022-08-26 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='authoer',
            new_name='author',
        ),
    ]