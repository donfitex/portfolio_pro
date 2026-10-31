from django.contrib import admin
from .models import About, Skill, Project, Contact
admin.site.site_header = 'Raphael Eze · Portfolio studio'
admin.site.site_title = 'Portfolio studio'
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'published', 'sort_order')
    list_editable = ('featured', 'published', 'sort_order')
    list_filter = ('category', 'published', 'featured')
    search_fields = ('title', 'description', 'tech_stack')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    def has_add_permission(self, request): return False
admin.site.register(About)
admin.site.register(Skill)
