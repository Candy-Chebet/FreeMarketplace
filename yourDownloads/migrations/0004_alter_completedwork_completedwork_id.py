# Generated by Django 4.1.13 on 2024-03-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourDownloads', '0003_alter_completedwork_completedwork_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedwork',
            name='completedWork_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
