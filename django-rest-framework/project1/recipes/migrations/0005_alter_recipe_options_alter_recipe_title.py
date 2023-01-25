# Generated by Django 4.0 on 2022-02-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=65, verbose_name='Title'),
        ),
    ]