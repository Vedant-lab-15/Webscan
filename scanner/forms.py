from django import forms

class ScanForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Enter Code/URL')
