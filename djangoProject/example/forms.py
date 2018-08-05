from django import forms
from django.forms import ModelForm
from .models import Product, Comment

degree_choices = [("degree1", "B-Tech"),
                  ("degree2", "B.Sc"), ("degree3", "B.Com"),
                  ("degree4", "B.A"), ("degree5", "M.Sc")
                  ]

class NameForm(forms.Form):
    your_name = forms.CharField(label="Full Name")
    your_age = forms.IntegerField(label="Age")
    degree = forms.CharField(
        label="Highest Degree", widget=forms.CheckboxSelectMultiple(choices=degree_choices)
    )
    date_field = forms.DateField(label="Birth Date",
        widget=forms.SelectDateWidget(years=[x for x in range(1980, 2030)])
    )

    def clean_your_age(self):
        your_age = self.cleaned_data.get("your_age")
        if your_age < 18:
            raise forms.ValidationError("Age Must be greater than 18")
        else:
            return your_age

class NewForm(forms.Form):
    name = forms.CharField()
    age  = forms.IntegerField()
    qualification = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()

#
#
# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['product_title', 'product_price', 'product_desc', 'date']
#         # exclude = ('date')

class MyCommentForm(ModelForm):
    # form logic
    class Meta:
        model = Comment
        fields = ['title', 'text', 'notes']


