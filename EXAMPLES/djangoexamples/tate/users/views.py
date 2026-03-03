#from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

# example without template
# def home(request):
#     return HttpResponse("Welcome to Users")

# example with template (normal Django approach)
def home(request):
    context = { 
        'message': "Welcome to Users",
        'homepage': True,  # don't add "return to home page" on home page
    }
    return render(request, 'users/home.html', context)
