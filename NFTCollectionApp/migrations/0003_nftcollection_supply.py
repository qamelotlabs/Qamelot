# Generated by Django 3.0.5 on 2022-06-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTCollectionApp', '0002_nftcollection_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcollection',
            name='supply',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
