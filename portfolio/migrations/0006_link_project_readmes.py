from django.db import migrations

def link_readmes(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    for project in Project.objects.filter(readme_link=''):
        if project.github_link and project.github_link.startswith('https://github.com/donfitex/') and project.github_link.rsplit('/', 1)[-1] != 'portfolio':
            project.readme_link = project.github_link.rstrip('/') + '/blob/main/README.md'
            project.save(update_fields=['readme_link'])

class Migration(migrations.Migration):
    dependencies = [('portfolio', '0005_project_readme_link')]
    operations = [migrations.RunPython(link_readmes, migrations.RunPython.noop)]
