from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({
            "name": "Raphael Eze",
            "profession": "Full-Stack Developer",
            "skills": ["Python", "Django", "JavaScript", "React", "HTML", "CSS"],
            "projects": [
                {
                    "name": "Project 1",
                    "description": "A simple web application built with Django and React."
                },
                {
                    "name": "Project 2",
                    "description": "A RESTful API built with Django REST Framework."
                },
                {
                    "name": "Project 3",
                    "description": "A personal portfolio website built with React and hosted on Netlify."
                },
                {
                    "name": "Project 4",
                    "description": "A mobile application built with React Native."
                },
                {
                    "name": "Project 5",
                    "description": "A machine learning project built with Python and scikit-learn."
                },
                {
                    "name": "Project 6",
                    "description": "An e-commerce website built with Django and Stripe for payment processing."
                },
                {
                    "name": "Project 7",
                    "description": "A social media platform built with Django and React."
                },
                {
                    "name": "Project 8",
                    "description": "A blog website built with Django and Markdown."
                },
                {
                    "name": "Project 9",
                    "description": "A task management application built with Django and React."
                },
                {
                    "name": "Project 10",
                    "description": "A weather application built with Django and OpenWeatherMap API."
                },
                {
                    "name": "Project 11",
                    "description": "A real-time chat application built with Django and WebSockets."
                },
                {
                    "name": "Project 12",
                    "description": "A cryptocurrency tracking application built with Django and CoinGecko API."
                },
                {
                    "name": "Project 13",
                    "description": "A movie recommendation system built with Django and scikit-learn."
                },
                {
                    "name": "Project 14",
                    "description": "A recipe sharing platform built with Django and React."
                },
                {
                    "name": "Project 15",
                    "description": "A fitness tracking application built with Django and React Native."
                },
                {
                    "name": "Project 16",
                    "description": "A travel planning application built with Django and React."
                },
                {
                    "name": "Project 17",
                    "description": "A language learning platform built with Django and React."
                },
                {
                    "name": "Project 18",
                    "description": "A stock market analysis tool built with Django and Plotly."
                },
                {
                    "name": "Project 19",
                    "description": "A personal finance management application built with Django and React."
                },
                {
                    "name": "Project 20",
                    "description": "A virtual reality application built with Django and A-Frame."
                },
                {
                    "name": "Project 21",
                    "description": "A music streaming platform built with Django and React."
                },
                {
                    "name": "Project 22",
                    "description": "A news aggregation website built with Django and React."
                },
                {
                    "name": "Project 23",
                    "description": "A job board platform built with Django and React."
                },
                {
                    "name": "Project 24",
                    "description": "A crowdfunding platform built with Django and Stripe for payment processing."
                },
                {
                    "name": "Project 25",
                    "description": "A virtual event platform built with Django and WebRTC."
                },
                {
                    "name": "Project 26",
                    "description": "A food delivery application built with Django and React Native."
                },
                {
                    "name": "Project 27",
                    "description": "A real estate listing platform built with Django and React."
                },
                {
                    "name": "Project 28",
                    "description": "A travel blog website built with Django and Markdown."
                },
                {
                    "name": "Project 29",
                    "description": "A personal budgeting tool built with Django and React."
                },
                {
                    "name": "Project 30",
                    "description": "A virtual classroom platform built with Django and WebRTC."
                }
            ],

            "message": "Welcome to my portfolio API. This API provides information about my skills, projects, and contact details. Feel free to explore the endpoints and learn more about my work.",
    })