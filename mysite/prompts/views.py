from django.http import HttpResponse

def index(request):
    return HttpResponse("helo, wordl youa re the prmpts index.")
