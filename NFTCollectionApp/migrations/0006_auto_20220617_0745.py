# Generated by Django 3.0.5 on 2022-06-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTCollectionApp', '0005_auto_20220617_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcollection',
            name='createdAt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nftcollection',
            name='updatedAt',
            field=models.DateField(blank=True, null=True),
        ),
    ]