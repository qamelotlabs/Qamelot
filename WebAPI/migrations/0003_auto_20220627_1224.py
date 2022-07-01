# Generated by Django 3.0.5 on 2022-06-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAPI', '0002_auto_20220627_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='username',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='userdetail',
            name='lastname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]