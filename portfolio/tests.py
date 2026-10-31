from django.test import TestCase, override_settings
from django.core.management import call_command
from django.contrib.auth import get_user_model
from portfolio.models import Project, Contact

@override_settings(SECURE_SSL_REDIRECT=False, STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class PortfolioTests(TestCase):
    def test_public_browsing_and_hidden_projects(self):
        Project.objects.create(title='Visible', description='<script>alert(1)</script>')
        Project.objects.create(title='Hidden', description='private', published=False)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Visible')
        self.assertNotContains(response, '<script>alert(1)</script>')
        self.assertNotContains(response, '>Hidden<')
        response = self.client.get('/api/projects/')
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(self.client.get('/health/').json(), {'status': 'ok'})
    def test_contact_validation_and_private_inbox(self):
        url = '/api/contact/'
        self.assertEqual(self.client.post(url, {'name': 'Alex', 'email': 'bad', 'message': 'x'}).status_code, 400)
        self.assertEqual(self.client.post(url, {'name': 'Alex', 'email': 'a@example.com', 'message': 'A project enquiry for you.'}).status_code, 201)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertEqual(self.client.get('/admin/portfolio/contact/').status_code, 302)
    def test_only_owner_can_edit(self):
        self.assertEqual(self.client.post('/api/projects/', {'title':'hacked'}).status_code, 405)
        user = get_user_model().objects.create_superuser('owner', 'owner@example.com', 'a-test-only-password')
        self.client.force_login(user)
        self.assertEqual(self.client.get('/admin/portfolio/project/add/').status_code, 200)
    def test_seed_preserves_owner_edits(self):
        call_command('seed_portfolio')
        project = Project.objects.first()
        project.title = 'Owner edited title'; project.published = False; project.save()
        count = Project.objects.count()
        call_command('seed_portfolio')
        project.refresh_from_db()
        self.assertEqual(project.title, 'Owner edited title')
        self.assertFalse(project.published)
        self.assertEqual(Project.objects.count(), count)
