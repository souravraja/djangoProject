# Generated by Django 4.0.4 on 2023-02-18 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ownshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=1000)),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_ownername', models.CharField(max_length=100)),
                ('ph_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product_details', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='productimage')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ownshop.ownshop')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='imagefolder')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ownshop.product')),
            ],
        ),
    ]
