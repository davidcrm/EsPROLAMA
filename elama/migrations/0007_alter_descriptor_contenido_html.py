# Generated by Django 5.1.8 on 2025-05-01 12:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elama', '0006_volcado_logro_volcado_mejora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptor',
            name='contenido_html',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
