from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates the initial admin user with username "sss" and password "sss"'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='sss').exists():
            User.objects.create_superuser('sss', 'sss@gmail.com', 'sss')
            self.stdout.write(self.style.SUCCESS('Successfully created superuser "sss"'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "sss" already exists'))
