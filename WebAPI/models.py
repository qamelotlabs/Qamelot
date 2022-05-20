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
    type = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)
    representation = models.CharField(max_length=100)
    mimeType = models.CharField(max_length=100)
    size = models.CharField(max_length=100, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Assets Image'


class APIPaginate(models.Model):
    total = models.CharField(max_length=100, blank=True)
    continuation = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'API Paginate'


class AssetsCollection(models.Model):
    banner_image_url = models.CharField(max_length=100)
    chat_url = models.CharField(max_length=100, blank=True)
    created_date = models.CharField(max_length=100)
    default_to_fiat = models.BooleanField()
    description = models.TextField(blank=True, default='')
    dev_buyer_fee_basis_points = models.CharField(max_length=100, blank=True)
    dev_seller_fee_basis_points = models.CharField(max_length=100, blank=True)
    discord_url = models.CharField(max_length=100, blank=True)
    card_display_style = models.CharField(max_length=100, blank=True)
    external_url = models.CharField(max_length=100, blank=True)
    featured = models.BooleanField()
    featured_image_url = models.CharField(max_length=100, blank=True)
    hidden = models.BooleanField()
    safelist_request_status = models.CharField(max_length=100, blank=True)
    image_url = models.CharField(max_length=100, blank=True)
    is_subject_to_whitelist = models.CharField(max_length=100, blank=True)
    large_image_url = models.CharField(max_length=100, blank=True)
    medium_username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    only_proxied_transfers = models.BooleanField()
    opensea_buyer_fee_basis_points = models.CharField(
        max_length=100, blank=True)
    opensea_seller_fee_basis_points = models.CharField(
        max_length=100, blank=True)
    payout_address = models.CharField(max_length=100, blank=True)
    require_email = models.BooleanField()
    short_description = models.TextField(blank=True, default='')
    slug = models.CharField(max_length=100, blank=True)
    telegram_url = models.CharField(max_length=100, blank=True)
    twitter_username = models.CharField(max_length=100, blank=True)
    instagram_username = models.CharField(max_length=100, blank=True)
    wiki_url = models.CharField(max_length=100, blank=True)
    is_nsfw = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Assets Collection'


class Assets(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    blockchain = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    tokenId = models.CharField(max_length=100)
    owner_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='owner_id', blank=True, null=True
    )
    creator_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='creator_id', blank=True, null=True
    )
    mintedAt = models.CharField(max_length=100)
    lastUpdatedAt = models.CharField(max_length=100)
    supply = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, default='')
    image_id = models.ForeignKey(
        AssetsImage, on_delete=models.CASCADE, related_name='image_id', blank=True, null=True
    )
    permalink = models.CharField(max_length=100, blank=True)
    restriction = models.CharField(max_length=100, blank=True)
    deleted = models.BooleanField(default=False)
    auction = models.CharField(max_length=100, blank=True)
    totalStock = models.CharField(max_length=100, blank=True)
    sellers = models.IntegerField(default=0, blank=True)
    status = models.CharField(max_length=100, blank=True)
    platform = models.CharField(max_length=100, blank=True)
    asset_collection = models.ForeignKey(
        AssetsCollection, on_delete=models.CASCADE, related_name='asset_collection', blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Asset'
