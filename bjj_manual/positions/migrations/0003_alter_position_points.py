# Generated by Django 4.2 on 2023-05-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("positions", "0002_move"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="points",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]