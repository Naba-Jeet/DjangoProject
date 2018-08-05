from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

# importing loading from django template
from django.template import loader
from django.utils import timezone

from .models import models, Product
from .forms import MyCommentForm,NameForm


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


def basic_form(request):
    # initial_dict = {
    #     "your_name": "Your Name Goes here",
    #     "your_age": 18
    # }
    form = NameForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        return render(request, "posts/thanks.html")
    return render(request, "posts/basic_form.html", {'form': form})
    # else:
    #     form = NameForm()
    #     return render(request, "posts/basic_form.html", {'form': form})

def add_model(request):
    if request.method == "POST":
        print(request.POST)
        form = MyCommentForm(request.POST)
        if form.is_valid():
            # model_instance = form.save(commit=False)
            # model_instance.timestamp = timezone.now()
            form.save()
            return render(request, "posts/thanks.html")
    else:
        form = MyCommentForm()
        return render(request, "posts/my_template.html", {'avishek': form})


