# Generated by Django 3.0 on 2022-05-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
