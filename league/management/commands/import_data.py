from django.core.management.base import BaseCommand
from league.models import Table

class Command(BaseCommand):
    help = 'Import data from league.txt file'


    def handle(self, *args, **kwargs):
        read_data = 'league\League_Table.txt'
        with open(read_data) as file:
            for line in file:
                data = line.strip().split(',')
                Table.objects.create(
                    team=data[0],
                    played = data[1],
                    goal_diff = data[2],
                    points = data[3]
                    )
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))