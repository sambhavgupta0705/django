from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello</h1>")

def about(request):
    return HttpResponse("I am about page")
 
