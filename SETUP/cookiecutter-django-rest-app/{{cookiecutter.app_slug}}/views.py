# not needed for REST CBVs or Viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your RESTful views here.

# example without template (only used in class -- always use templates in real life):
@api_view(['GET'])
def hello(request):
     return Response('{"message": "Welcome to {{ cookiecutter.app_name }}"}', 200)

