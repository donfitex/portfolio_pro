from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({
            "name": "Raphael Eze",
            "profession": "Backend Developer",
            "message": "Welcome to my portfolio API. This API provides information about my skills, projects, and contact details. Feel free to explore the endpoints and learn more about my work.",
    })