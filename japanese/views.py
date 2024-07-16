from django.http import HttpResponse


def index(request):
    welcome_text = "Hello, welcome! You have reached JPN learning"
    return HttpResponse(welcome_text)


def input(request):
    return HttpResponse("This is where new characters are fed")
