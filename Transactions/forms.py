from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'Task', 'Budget','Status',
                  
                'comments', 'invoice_number', 'invoice_date', 'name',       
                'Task', 'Category','Budget', 'Currency','paymentPeriod', 'Status' 
    
				]

    def clean_invoice_date(self):
     invoice_date = self.cleaned_data.get('invoice_date')
     if not invoice_date:
         raise forms.ValidationError('This field is required')
     return invoice_date
 
    def clean_name(self):
     name = self.cleaned_data.get('name')
     if not name:
         raise forms.ValidationError('This field is required')
     return name

    def clean_Task(self):
         Task = self.cleaned_data.get('Task')
         if not Task:
             raise forms.ValidationError('This field is required')
         return Task

    def clean_Category(self):
         Category = self.cleaned_data.get('Category')
         if not Category:
             raise forms.ValidationError('This field is required')
         return Category
     
    # def clean_emailAddress(self):
    #      emailAddress = self.cleaned_data.get('emailAddress')
    #      if not emailAddress:
    #          raise forms.ValidationError('This field is required')
    #      return emailAddress
     
    def clean_Budget(self):
         Budget = self.cleaned_data.get('Budget')
         if not Budget:
             raise forms.ValidationError('This field is required')
         return Budget

    def clean_paymentPeriod(self):
         paymentPeriod = self.cleaned_data.get('paymentPeriod')
         if not paymentPeriod:
             raise forms.ValidationError('This field is required')
         return paymentPeriod
     
    def clean_Status(self):
         Status = self.cleaned_data.get('Status')
         if not Status:
             raise forms.ValidationError('This field is required')
         return Status

class InvoiceSearchForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name']
        
        
class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'Task', 'Budget','Status',
                  
                'comments', 'invoice_number', 'invoice_date', 'name',       
                'Task', 'Category','Budget', 'Currency','paymentPeriod', 'Status' 
    
				]

    def clean_invoice_date(self):
     invoice_date = self.cleaned_data.get('invoice_date')
     if not invoice_date:
         raise forms.ValidationError('This field is required')
     return invoice_date
 
    def clean_name(self):
     name = self.cleaned_data.get('name')
     if not name:
         raise forms.ValidationError('This field is required')
     return name

    def clean_Task(self):
         Task = self.cleaned_data.get('Task')
         if not Task:
             raise forms.ValidationError('This field is required')
         return Task

    def clean_Category(self):
         Category = self.cleaned_data.get('Category')
         if not Category:
             raise forms.ValidationError('This field is required')
         return Category
     
    # def clean_emailAddress(self):
    #      emailAddress = self.cleaned_data.get('emailAddress')
    #      if not emailAddress:
    #          raise forms.ValidationError('This field is required')
    #      return emailAddress
     
    def clean_Budget(self):
         Budget = self.cleaned_data.get('Budget')
         if not Budget:
             raise forms.ValidationError('This field is required')
         return Budget

    def clean_paymentPeriod(self):
         paymentPeriod = self.cleaned_data.get('paymentPeriod')
         if not paymentPeriod:
             raise forms.ValidationError('This field is required')
         return paymentPeriod
     
    def clean_Status(self):
         Status = self.cleaned_data.get('Status')
         if not Status:
             raise forms.ValidationError('This field is required')
         return Status
