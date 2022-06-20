# Generated by Django 3.0.5 on 2022-06-17 12:28

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionSeedStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Nft Influencers',
            },
        ),
        migrations.CreateModel(
            name='NftInfluencers',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('verified', models.BooleanField(default=True)),
                ('created_at', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Nft Influencers',
            },
        ),
        migrations.CreateModel(
            name='TweetData',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('author_id', models.CharField(blank=True, max_length=100)),
                ('collection_id', models.CharField(blank=True, max_length=100)),
                ('lang', models.CharField(max_length=10)),
                ('retweet_count', models.IntegerField(blank=True, default=0)),
                ('reply_count', models.IntegerField(blank=True, default=0)),
                ('like_count', models.IntegerField(blank=True, default=0)),
                ('quote_count', models.IntegerField(blank=True, default=0)),
                ('twitter_text', models.TextField()),
                ('in_reply_to_user_id', models.CharField(max_length=100)),
                ('referenced_tweets', jsonfield.fields.JSONField(default=dict)),
                ('mentions', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'verbose_name': 'Tweet Data',
            },
        ),
        migrations.CreateModel(
            name='TwitterUsers',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=254)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('followers_count', models.IntegerField(blank=True, default=0)),
                ('following_count', models.IntegerField(blank=True, default=0)),
                ('tweet_count', models.IntegerField(blank=True, default=0)),
                ('listed_count', models.IntegerField(blank=True, default=0)),
                ('verified', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=100)),
                ('created_at', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Twitter User',
            },
        ),
    ]
