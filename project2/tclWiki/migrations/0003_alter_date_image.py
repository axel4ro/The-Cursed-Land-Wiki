# Generated by Django 5.0.6 on 2024-07-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tclWiki', '0002_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]