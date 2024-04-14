from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp2.models import Client


class Command(BaseCommand):
    help = "Creates clients in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client(
            name="Ivan",
            email="Ivan@gmail.com",
            phone_number="+793234544554",
            address="Moscow, Red square",
            registration_date=date(year=2024, month=4, day=14),
        )
        client.save()
        self.stdout.write(f"{client}")
