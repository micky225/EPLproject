# Generated by Django 4.2.3 on 2023-07-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_remove_header_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_a', models.CharField(max_length=200)),
                ('team_b', models.CharField(max_length=200)),
                ('team_c', models.CharField(max_length=200)),
                ('team_d', models.CharField(max_length=200)),
                ('team_e', models.CharField(max_length=200)),
                ('team_f', models.CharField(max_length=200)),
                ('team_g', models.CharField(max_length=200)),
                ('team_h', models.CharField(max_length=200)),
                ('team_i', models.CharField(max_length=200)),
                ('team_j', models.CharField(max_length=200)),
                ('team_k', models.CharField(max_length=200)),
                ('team_l', models.CharField(max_length=200)),
                ('team_m', models.CharField(max_length=200)),
                ('team_n', models.CharField(max_length=200)),
                ('team_o', models.CharField(max_length=200)),
                ('team_p', models.CharField(max_length=200)),
                ('team_q', models.CharField(max_length=200)),
                ('team_r', models.CharField(max_length=200)),
                ('team_s', models.CharField(max_length=200)),
                ('team_t', models.CharField(max_length=200)),
            ],
        ),
    ]
