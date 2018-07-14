from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# importing loading from django template
from django.template import loader

from .models import models

def index(request):
    template_path = "posts/index.html"
    context_dictionary = {'title': 'Latest Posts'}
    return render(request, template_path, context_dictionary)

def post_model_list_view(request):
    template_path= "index.html"
    context_dictionary ={'title':'Latest Posts'}
    return render(request , template_path , context_dictionary)