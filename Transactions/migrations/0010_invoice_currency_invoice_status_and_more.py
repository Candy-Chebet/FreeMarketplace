# Generated by Django 5.0 on 2024-01-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0009_remove_invoice_balance_remove_invoice_last_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='Currency',
            field=models.CharField(choices=[('$', 'USD'), ('Ksh', 'KSH')], default='$', max_length=200),
        ),
        migrations.AddField(
            model_name='invoice',
            name='Status',
            field=models.CharField(choices=[('Current', 'Current'), ('Pending', 'Pending'), ('Paid', 'Paid')], default='Current', max_length=250),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paymentPeriod',
            field=models.CharField(choices=[('14 days', '14 days'), ('30 days', '30 days'), ('60 days', '60 days')], default='14 days', max_length=250),
        ),
    ]