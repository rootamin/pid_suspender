from django import forms

class ProcessForm(forms.Form):
    pid = forms.IntegerField(label='Enter PID', required=True)