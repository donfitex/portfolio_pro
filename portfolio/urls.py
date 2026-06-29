from django.urls import path
from .views import home, about, skills, projects, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]