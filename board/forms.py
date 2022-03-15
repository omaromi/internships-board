from django import forms

class IntUpload(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    position_title = forms.CharField(max_length=200)
    # date_posted = forms.DateField(default=date.today)
    app_link= forms.URLField()
    description = forms.CharField(max_length=500)