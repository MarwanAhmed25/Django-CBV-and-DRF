# Generated by Django 4.1.4 on 2022-12-30 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_types", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="type",
            name="title",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
