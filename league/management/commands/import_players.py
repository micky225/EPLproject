from django.core.management.base import BaseCommand
from league.models import Statistics
import pandas as pd
import openpyxl

class Command(BaseCommand):
    help = 'Import data from Top_player.xlsx file'

    def handle(self, *args, **kwargs):
        df = pd.read_excel('league\Top_Players.xlsx')
        for index, row in df.iterrows():
            Statistics.objects.create(
                goals=row['Goals'],
                assists=row['Assists'],
                goals_assits=row['Goals + Assists'],
                penalty_goals=row['Penalty Goals'],
                freekick_goals=row['Free Kick Goals'],
                yellow_cards=row['Yellow Cards'],
                red_cars=row['Red Cards'],
                penalties_won=row['Penalties Won'],
                chances_created=row['Chances Ceated'],
                chances_missed=row['Chances Missed'],
                acc_pass_per_g=row['Acc. Pass per Game'],
                succ_dribbles=row['Succ. Dribbles per game'],
                clearances=row['Clearances. Per Game'],
                clean_sheet=row['Clean Sheets']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))