# Generated by Django 4.0.4 on 2022-05-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_data_alter_qr_cdate_alter_qr_ctime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door', models.CharField(max_length=10)),
            ],
        ),
    ]
