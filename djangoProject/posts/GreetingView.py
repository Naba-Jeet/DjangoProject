from django.http import HttpResponse
from django.views import View

class GreetingView(View):
    greeting = "This Is a formal Greeting"
    def get(self , request):
        return HttpResponse(self.greeting)
