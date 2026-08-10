from time import sleep

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError as DjangoOperationalError
from psycopg import OperationalError as PsycopgOperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                db_con = connections["default"]
                db_con.cursor()
                db_up = True
            except (DjangoOperationalError, PsycopgOperationalError):
                self.stdout.write("Database unavailable waiting 3 seconds...")
                sleep(3)

        self.stdout.write(self.style.SUCCESS("Database available!"))
