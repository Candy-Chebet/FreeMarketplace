# Generated by Django 4.1.13 on 2024-03-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourDownloads', '0002_remove_completedwork_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='completedWork_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]