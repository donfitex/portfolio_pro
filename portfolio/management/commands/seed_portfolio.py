import json
from pathlib import Path
from django.core.management.base import BaseCommand
from portfolio.models import Project
class Command(BaseCommand):
    help = 'Import reviewed GitHub projects without overwriting owner edits'
    def handle(self, *args, **kwargs):
        rows = json.loads((Path(__file__).resolve().parents[2] / 'data/projects.json').read_text())
        for row in rows:
            Project.objects.get_or_create(github_link=row['github_link'], defaults={k:v for k,v in row.items() if k != 'github_link'})
        self.stdout.write(f'Reviewed {len(rows)} projects; existing edits preserved.')
