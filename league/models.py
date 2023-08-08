from django.db import models

# Create your models here.
class Table(models.Model):
    team =  models.CharField(max_length=200,)
    played = models.CharField(max_length=200,)
    goal_diff =  models.CharField(max_length=200,)
    points =  models.CharField(max_length=200,)
    


class Header(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True)
    # details = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.title}'


class Players(models.Model):
    team_a = models.CharField(max_length=200)
    team_b = models.CharField(max_length=200)
    team_c = models.CharField(max_length=200)
    team_d = models.CharField(max_length=200)
    team_e = models.CharField(max_length=200)
    team_f = models.CharField(max_length=200)
    team_g = models.CharField(max_length=200)
    team_h = models.CharField(max_length=200)
    team_i = models.CharField(max_length=200)
    team_j = models.CharField(max_length=200)
    team_k = models.CharField(max_length=200)
    team_l = models.CharField(max_length=200)
    team_m = models.CharField(max_length=200)
    team_n = models.CharField(max_length=200)
    team_o = models.CharField(max_length=200)
    team_p = models.CharField(max_length=200)
    team_q = models.CharField(max_length=200)
    team_r = models.CharField(max_length=200)
    team_s = models.CharField(max_length=200)
    team_t = models.CharField(max_length=200)


class Statistics(models.Model):
    goals = models.CharField(max_length=200)
    assists = models.CharField(max_length=200)
    goals_assits = models.CharField(max_length=200)
    penalty_goals = models.CharField(max_length=200)
    freekick_goals = models.CharField(max_length=200)
    yellow_cards = models.CharField(max_length=200)
    red_cars = models.CharField(max_length=200)
    penalties_won = models.CharField(max_length=200)
    chances_created = models.CharField(max_length=200)
    chances_missed = models.CharField(max_length=200)
    acc_pass_per_g = models.CharField(max_length=200)
    succ_dribbles = models.CharField(max_length=200)
    clearances = models.CharField(max_length=200)
    clean_sheet = models.CharField(max_length=200)



