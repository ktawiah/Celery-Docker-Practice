# Generated by Django 5.0.6 on 2024-05-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_accounts", "0003_rename_avatar_user__avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="_avatar",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images",
                verbose_name="profile picture",
            ),
        ),
    ]
