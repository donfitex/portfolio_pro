from django.contrib import admin
from .models import About, Skill, Project, Contact

# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)