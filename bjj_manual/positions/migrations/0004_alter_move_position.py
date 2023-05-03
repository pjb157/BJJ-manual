# Generated by Django 4.2 on 2023-05-03 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("positions", "0003_alter_position_points"),
    ]

    operations = [
        migrations.AlterField(
            model_name="move",
            name="position",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="moves",
                to="positions.position",
            ),
        ),
    ]
