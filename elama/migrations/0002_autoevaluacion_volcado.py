# Generated by Django 5.0.6 on 2024-06-15 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autoevaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('finalizada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'autoevaluaciones',
            },
        ),
        migrations.CreateModel(
            name='Volcado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.CharField(max_length=1)),
                ('autoevaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elama.autoevaluacion')),
                ('descriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elama.descriptor')),
            ],
        ),
    ]
