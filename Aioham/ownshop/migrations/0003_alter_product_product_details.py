# Generated by Django 3.2 on 2023-04-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownshop', '0002_auto_20230408_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(default=None),
        ),
    ]
