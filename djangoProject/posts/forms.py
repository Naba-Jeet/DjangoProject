from django import forms
from django.forms import ModelForm
from .models import Product, Comment


# class NameForm(forms.Form):
#     your_name = forms.CharField()
#     your_age = forms.DateField()
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
