from django.core.management.base import BaseCommand
from league.models import Players
import pandas as pd
import openpyxl


class Command(BaseCommand):
    help = 'Import data from Players.xlsx'


    def handle(self, *args, **kwargs):
        data = pd.read_excel('league/Players.xlsx')
        for index, row in data.iterrows():
            Players.objects.create(
                team_a=row['Man.City'],
                team_b=row['Arsenal'],
                team_c=row['Newcastle'],
                team_d=row['Man.United'],
                team_e=row['Liverpool'],
                team_f=row['Tottenham'],
                team_g=row['Aston Villa'],
                team_h=row['Brighton'],
                team_i=row['Fulham'],
                team_j=row['Brentford'],
                team_k=row['Chelsea'],
                team_l=row['Crystal Palace'],
                team_m=row['Wolves'],
                team_n=row['Bournemouth'],
                team_o=row['West Ham'],
                team_p=row['Forest'],
                team_q=row['Everton'],
                team_r=row['Leeds'],
                team_s=row['Leicester'],
                team_t=row['Southampton']

            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))    