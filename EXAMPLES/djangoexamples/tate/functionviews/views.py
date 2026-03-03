#from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.

# example without template
# def home(request):
#     return HttpResponse("Welcome to Function-based Views Demo")

# example with template (normal Django approach)
def home(request):
    context = { 
        'message': "Welcome to Function-based Views Demo",
    }
    return render(request, 'functionviews/home.html', context)
