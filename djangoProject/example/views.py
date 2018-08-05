from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

# importing loading from django template
from django.template import loader
from django.utils import timezone

from .models import models, Product
from .forms import MyCommentForm, NameForm, NewForm


# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def add_model(request):
    if request.method == "POST":
        print(request.POST)
        form = NewForm(request.POST)
        if form.is_valid():
            # model_instance = form.save(commit=False)
            # model_instance.timestamp = timezone.now()
            #form.save()
            return render(request, "posts/thanks.html")
    else:
        form = NewForm()
        return render(request, "posts/my_template.html", {'avishek': form})

