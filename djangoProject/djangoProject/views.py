from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    print(request.method)
    response = HttpResponse(content_type='text/html') #TODO Check other content types
    response.write("<h2>Home Page</h2>")
    response.status_code = 200
    return response