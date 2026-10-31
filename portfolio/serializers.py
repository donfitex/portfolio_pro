from rest_framework import serializers
from .models import About, Skill, Project, Contact

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)
    message = serializers.CharField(max_length=5000, min_length=10)
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
