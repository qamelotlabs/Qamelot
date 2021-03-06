# Generated by Django 3.0.5 on 2022-06-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TwitterApp', '0002_auto_20220623_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=555)),
                ('username', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('userImageUrl', models.CharField(blank=True, max_length=255)),
                ('createdAt', models.DateField(blank=True, null=True)),
                ('updatedAt', models.DateField(blank=True, null=True)),
                ('influencers', models.ManyToManyField(to='TwitterApp.NftInfluencers')),
            ],
            options={
                'verbose_name': 'User Detail',
            },
        ),
    ]
