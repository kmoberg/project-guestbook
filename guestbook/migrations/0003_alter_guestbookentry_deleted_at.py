# Generated by Django 5.1 on 2024-08-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guestbook", "0002_alter_guestbookentry_deleted_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guestbookentry",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
