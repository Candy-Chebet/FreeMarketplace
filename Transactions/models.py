from django.db import models
from django.utils import timezone
from uuid import uuid4
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse



class Invoice(models.Model):
    
    CATEGORIES = [
        ('Programming', 'Programming'),
        ('Literature', 'Literature'),
        ('Graphic Design', 'Graphic Design'),
        ('Research', 'Research'),
        ('Other', 'Other'),
    ]
    TERMS = [
        ('14 days', '14 days'),
        ('30 days', '30 days'),
    ]
    
    CURRENCY = [
        ('$', 'USD'),
        ('Ksh', 'KSH'),
    ]
    STATUS= [
        ('Current', 'Current'),
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]  
    comments = models.TextField(max_length=3000, default='', blank=True, null=True)
    invoice_number = models.IntegerField(null=True, blank=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
    emailAddress = models.CharField(null=True, max_length=250) 
    
    Task = models.CharField('Task', max_length=120, default='', blank=True, null=True)
    Category = models.CharField(choices=CATEGORIES, null=True, blank=True, max_length=200)
    Budget = models.IntegerField('Amount', default=0, blank=True, null=True)
    Currency = models.CharField(choices=CURRENCY, default='$', max_length=200)
    paymentPeriod = models.CharField(choices = TERMS, null=True, blank=True, max_length=200)
    Status = models.CharField(choices=STATUS, default='Current', max_length=250)
    

    Invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Proforma Invoice', 'Proforma Invoice'),
        ('Invoices', 'Invoices'),
    )

    invoice_type = models.CharField(max_length=50, default='', blank = True, null=True, choices=Invoice_type_choice)

    def __str__(self):
        return self.name
    

