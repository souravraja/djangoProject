# Generated by Django 3.2 on 2023-04-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownshop', '0003_alter_product_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]