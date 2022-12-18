# Generated by Django 4.1.2 on 2022-10-19 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stolovka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tray',
            fields=[
                ('tray_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tray',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrayStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=1, unique=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'tray_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('student_card', models.CharField(max_length=8, unique=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='dorm',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foodtype',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id_tray', models.OneToOneField(db_column='id_tray', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stolovka.tray')),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'item',
                'managed': False,
            },
        ),
    ]
