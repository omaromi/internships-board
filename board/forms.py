from django import forms
from .models import Company, Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ('position_title','app_link','description', 'staff', 'company')

        labels = {
            'position_title':'Position Title',
            'app_link':'Link to Apply',
            'description':'Job Description',
            'staff':'Assigned Staff Member',
            'company':'Company',

        }

        widgets = {
            'position_title': forms.TextInput(attrs={'class':'form-control'}),
            'app_link': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'staff': forms.Select(attrs={'class':'form-control'}),
            'company': forms.Select(attrs={'class':'form-control'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'