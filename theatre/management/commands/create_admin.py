import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ.get("ADMIN_EMAIL", "admin@admin.com")
        password = os.environ.get("ADMIN_PASSWORD", "123456Pp")

        user, created = User.objects.get_or_create(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Create admin {email}")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f"Password for {email} update")
            )
