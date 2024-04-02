from django import forms
from .models import completedTaskss


required = 'Please fill in this field first!'
class CompletedTasksForm(forms.ModelForm):
    class Meta:
        model = completedTaskss
        fields = [ 'taskName', 'description', 'completionDate', 'attachment']
        
        
    def clean_taskName(self):
        taskName = self.cleaned_data.get('taskName')
        if not taskName:
            raise forms.ValidationError(required)
        return taskName
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError(required)
        return description
    
    def clean_attachment(self):
        attachment= self.cleaned_data.get('attachment')
        if not attachment:
            raise forms.ValidationError(required)
        return attachment


class updateCompletedTasksForm(forms.ModelForm):
    class Meta:
        model = completedTaskss
        fields = ['taskName', 'description', 'completionDate', 'attachment']
        
        
    def clean_taskName(self):
        taskName = self.cleaned_data.get('taskName')
        if not taskName:
            raise forms.ValidationError(required)
        return taskName
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError(required)
        return description
    
    def clean_attachment(self):
        attachment= self.cleaned_data.get('attachment')
        if not attachment:
            raise forms.ValidationError(required)
        return attachment
