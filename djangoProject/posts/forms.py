from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField()
    your_age = forms.DateField()


