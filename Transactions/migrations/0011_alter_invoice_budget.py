# Generated by Django 5.0 on 2024-01-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0010_invoice_currency_invoice_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Budget',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
