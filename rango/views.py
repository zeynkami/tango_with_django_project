from django.http import HttpResponse

def index(request):
    return Httpresponse('Rango says hey there partner! <a href="/rango/about/">About</a>')

def about(request):
    return HttpResponse('Rango says here is about the page. <a href="/rango/">Index</a>')




