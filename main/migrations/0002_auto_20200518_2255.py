# Generated by Django 3.0.6 on 2020-05-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="url",
            field=models.URLField(unique=True),
        ),
    ]
