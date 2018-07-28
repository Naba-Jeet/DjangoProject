from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

# importing loading from django template
from django.template import loader

from .models import models
from .forms import NameForm


def index(request):
    template_path = "posts/index.html"
    #data processing and logic
    context_dictionary = {'title': 'Latest Posts'}
    return render(request, template_path, context_dictionary)

def post_model_list_view(request):
    template_path= "index.html"
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    context_dictionary ={'title' : 'Latest Posts', 'numbers' : numbers}
    return render(request , template_path , context_dictionary)

def get_name(request):
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponseRedirect('/posts/thanks/')
    #
    # # if a GET (or any other method) we'll create a blank form
    # else:
    form = NameForm()

    return render(request, 'posts/name.html', {'form': form})