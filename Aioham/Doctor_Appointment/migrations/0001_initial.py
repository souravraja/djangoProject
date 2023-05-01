# Generated by Django 4.0.4 on 2023-04-12 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dieases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor_image', models.ImageField(blank=True, null=True, upload_to='doctorimage/')),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('license', models.FileField(blank=True, null=True, upload_to='doctordocument/')),
                ('license_image', models.ImageField(blank=True, null=True, upload_to='licenseimage/')),
                ('specalist', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor_Appointment.dieases')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamber', models.TextField(blank=True, null=True)),
                ('pinnumber', models.IntegerField()),
                ('opinngtime', models.TimeField()),
                ('closingtime', models.TimeField()),
                ('doctor', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor_Appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_age', models.IntegerField(blank=True, null=True)),
                ('bloodgroup', models.CharField(blank=True, choices=[('AB', 'AB+'), ('B', 'B+'), ('A', 'A+'), ('O', 'O+')], max_length=100, null=True)),
                ('appointment_date', models.DateTimeField()),
                ('doctor_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='Doctor_Appointment.doctor')),
            ],
        ),
    ]
