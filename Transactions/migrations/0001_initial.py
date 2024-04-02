# Generated by Django 5.0 on 2024-01-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=200, null=True)),
                ('emailAddress', models.CharField(max_length=250, null=True)),
                ('Task', models.CharField(blank=True, max_length=200, null=True)),
                ('Category', models.CharField(blank=True, choices=[('Programming', 'Programming'), ('Literature', 'Literature'), ('Graphic Design', 'Graphic Design'), ('Research', 'Research')], max_length=200, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(blank=True, max_length=200, null=True)),
                ('Task', models.CharField(blank=True, max_length=200, null=True)),
                ('Category', models.CharField(blank=True, max_length=200, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('Status', models.CharField(blank=True, max_length=200, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
