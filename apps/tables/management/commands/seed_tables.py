from django.core.management.base import BaseCommand
from apps.tables.models import RestaurantTable


class Command(BaseCommand):
    help = 'Seed restaurant tables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=8,
            help='Number of tables to create'
        )

    def handle(self, *args, **options):
        count = options['count']
        self.stdout.write(f'Creating {count} tables...')

        RestaurantTable.objects.all().delete()

        for i in range(1, count + 1):
            RestaurantTable.objects.create(table_number=i)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {count} tables!'
            )
        )