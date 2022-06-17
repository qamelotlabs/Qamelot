import jsonfield
from django.db import models
from datetime import datetime
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.contrib import admin
from imagekit.admin import AdminThumbnail
from django import forms


class TwitterUsers(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    url = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=100, blank=True)
    followers_count = models.IntegerField(default=0, blank=True)
    following_count = models.IntegerField(default=0, blank=True)
    tweet_count = models.IntegerField(default=0, blank=True)
    listed_count = models.IntegerField(default=0, blank=True)
    verified = models.BooleanField()
    username = models.CharField(max_length=100, blank=True)
    created_at = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Twitter User'

class TweetData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    author_id = models.CharField(max_length=100, blank=True)
    collection_id = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=10)
    retweet_count = models.IntegerField(default=0, blank=True)
    reply_count = models.IntegerField(default=0, blank=True)
    like_count = models.IntegerField(default=0, blank=True)
    quote_count = models.IntegerField(default=0, blank=True)
    twitter_text = models.TextField()
    in_reply_to_user_id = models.CharField(max_length=100)
    referenced_tweets = jsonfield.JSONField()
    mentions = jsonfield.JSONField()

    def __str__(self):
        return self.author_id
        
    class Meta:
        verbose_name = 'Tweet Data'

class NftInfluencers(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=True)
    created_at = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Nft Influencers'

class CollectionSeedStatus(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    collection_id = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.collection_id
        
    class Meta:
        verbose_name = 'Nft Influencers'