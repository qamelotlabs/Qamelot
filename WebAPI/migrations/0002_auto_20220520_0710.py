# Generated by Django 3.0 on 2022-05-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='id',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]