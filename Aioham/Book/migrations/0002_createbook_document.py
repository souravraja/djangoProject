# Generated by Django 4.0.4 on 2023-02-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createbook',
            name='document',
            field=models.FileField(default=None, upload_to='doc/'),
        ),
    ]