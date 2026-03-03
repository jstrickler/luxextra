#from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

# example without template
# def home(request):
#     return HttpResponse("Welcome to Django Messages Demo")

# example with template (normal Django approach)
def home(request):
    messages.info(request, "message info")
    messages.debug(request, "Debugging...")
    messages.warning(request, "WARNING WARNING")
    messages.error(request, "An error has occurred")

    context = { 
        'title': "Welcome to Django Messages Demo",
    }
    return render(request, 'messagesdemo/home.html', context)
