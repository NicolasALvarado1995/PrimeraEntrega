# Generated by Django 3.2.13 on 2022-04-25 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Muestro', '0005_auto_20220425_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='Muestro.curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesores', to='Muestro.profesor'),
        ),
    ]
