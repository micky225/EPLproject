# Generated by Django 4.2.3 on 2023-07-26 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_alter_table_goal_diff_alter_table_played_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='details',
        ),
    ]
