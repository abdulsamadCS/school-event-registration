from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='demo_user').exists():
            User.objects.create_superuser('demo_user', 'demo@example.com', 'demo_password')
            self.stdout.write(self.style.SUCCESS('Demo superuser created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Demo superuser already exists.'))