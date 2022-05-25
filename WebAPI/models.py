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


class AssetsUsers(models.Model):
    user_type = models.CharField(max_length=254)
    username = models.CharField(max_length=254, blank=True)
    profile_img_url = models.CharField(max_length=254, blank=True)
    address = models.CharField(max_length=254)
    value = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Assets User'


class AssetsImage(models.Model):
    type = models.CharField(max_length=255, blank=True)
    external_image_url = models.CharField(max_length=255)
    aws_bucket_image_url = models.CharField(max_length=255)
    representation = models.CharField(max_length=255)
    mimeType = models.CharField(max_length=255)
    size = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=255, blank=True)
    height = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Assets Image'


class APIPaginate(models.Model):
    total = models.CharField(max_length=255, blank=True)
    continuation = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'API Paginate'


class BestOrders(models.Model):
    order_id = models.CharField(max_length=255, blank=True)
    makeprice = models.CharField(max_length=255, blank=True)
    takeprice = models.CharField(max_length=255, blank=True)
    maker = models.CharField(max_length=255, blank=True)
    taker = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = 'Best Orders'


class AssetsCollection(models.Model):
    collection_id = models.CharField(max_length=255, blank=True)
    blockchain = models.CharField(max_length=255, blank=True)
    colletion_type = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, default='')
    symbol = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=255, blank=True)
    minters = models.CharField(max_length=255, blank=True)
    collection_image = models.ForeignKey(
        AssetsImage, on_delete=models.CASCADE, related_name='collection_image', blank=True, null=True
    )
    external_link = models.CharField(max_length=255, blank=True)
    fee_recipient = models.CharField(max_length=255, blank=True)
    best_order = models.ForeignKey(
        BestOrders, on_delete=models.CASCADE, related_name='best_order', blank=True, null=True
    )
    twitter_username = models.CharField(max_length=255, blank=True)
    discord_url = models.CharField(max_length=255, blank=True)
    seller_fee_basis_point = models.CharField(max_length=255, blank=True)
    buyer_fee_basis_point = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Assets Collection'


class Assets(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    blockchain = models.CharField(max_length=255)
    collection = models.CharField(max_length=255)
    contract = models.CharField(max_length=255)
    tokenId = models.CharField(max_length=255)
    owner_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='owner_id', blank=True, null=True
    )
    creator_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='creator_id', blank=True, null=True
    )
    mintedAt = models.CharField(max_length=255)
    lastUpdatedAt = models.CharField(max_length=255)
    supply = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, default='')
    image_id = models.ForeignKey(
        AssetsImage, on_delete=models.CASCADE, related_name='image_id', blank=True, null=True
    )
    permalink = models.CharField(max_length=255, blank=True)
    restriction = models.CharField(max_length=255, blank=True)
    deleted = models.BooleanField(default=False)
    auction = models.CharField(max_length=255, blank=True)
    totalStock = models.CharField(max_length=255, blank=True)
    sellers = models.IntegerField(default=0, blank=True)
    status = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=255, blank=True)
    asset_collection = models.ForeignKey(
        AssetsCollection, on_delete=models.CASCADE, related_name='asset_collection', blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asset'

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

class TwwetData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    author_id = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=10)
    retweet_count = models.IntegerField(default=0, blank=True)
    reply_count = models.IntegerField(default=0, blank=True)
    like_count = models.IntegerField(default=0, blank=True)
    quote_count = models.IntegerField(default=0, blank=True)
    text = models.TextField()
    in_reply_to_user_id = models.CharField(max_length=100)
    referenced_tweets = jsonfield.JSONField()
    mentions = jsonfield.JSONField()

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Tweet Data'