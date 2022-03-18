from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ('position_title','app_link','description', 'staff', 'company')

        labels = {
            'position_title':'',
            'app_link':'',
            'description':'',
            'staff':'',
            'company':'',

        }

        widgets = {
            'position_title': forms.TextInput(attrs={'class':'form-control'}),
            'app_link': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'staff': forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
        }

    # your_name = forms.CharField(label='Your name', max_length=100)
    # position_title = forms.CharField(max_length=200)
    # # date_posted = forms.DateField(default=date.today)
    # app_link= forms.URLField()
    # description = forms.CharField(max_length=500)