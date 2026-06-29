from django.db import models

# Create your models here.

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Me"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"