from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import About, Skill, Project, Contact
from .serializers import AboutSerializer, SkillSerializer, ProjectSerializer, ContactSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({
            "name": "Raphael Eze",
            "profession": "Full-Stack Developer",
            "message": "Welcome to my portfolio API. This API provides information about my skills, projects, and contact details. Feel free to explore the endpoints and learn more about my work.",
    })

@api_view(['GET'])
def about(request):
    about = About.objects.first()
    serializer = AboutSerializer(about)
    return Response(serializer.data)

@api_view(['GET'])
def skills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def contact(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "Thank you for reaching out! Your message has been sent successfully."
            },
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)