# Generated by Django 3.0.5 on 2022-06-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTCollectionApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcollection',
            name='created_at',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]