# Generated by Django 5.1 on 2024-08-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guestbook", "0004_guestbookentry_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="guestbookentry",
            name="irrelevant",
            field=models.BooleanField(default=False),
        ),
    ]
