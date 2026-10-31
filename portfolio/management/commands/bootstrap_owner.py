import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
class Command(BaseCommand):
    help = 'Create an owner once using OWNER_USERNAME, OWNER_EMAIL and OWNER_PASSWORD from secure environment'
    def handle(self, *args, **kwargs):
        password = os.getenv('OWNER_PASSWORD')
        if not password:
            return
        username = os.getenv('OWNER_USERNAME', 'raphael')
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            return
        user = User(username=username, email=os.getenv('OWNER_EMAIL', ''))
        validate_password(password, user)
        User.objects.create_superuser(username, user.email, password)
        self.stdout.write('Owner account created. Remove OWNER_PASSWORD from environment after first deployment.')
