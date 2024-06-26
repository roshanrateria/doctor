# Generated by Django 3.2.19 on 2024-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('receptionist', 'Receptionist')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
