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
    username = models.CharField(max_length=254)
    profile_img_url = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    config = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.username
        
    class Meta:
        verbose_name = 'Assets User'


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
    opensea_buyer_fee_basis_points = models.CharField(max_length=100, blank=True)
    opensea_seller_fee_basis_points = models.CharField(max_length=100, blank=True)
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
    token_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    image_url = models.CharField(max_length=100)
    image_preview_url = models.CharField(max_length=100, blank=True)
    image_thumbnail_url = models.CharField(max_length=100, blank=True)
    permalink = models.CharField(max_length=100)
    external_link = models.CharField(max_length=100, blank=True)
    asset_contract_id = models.CharField(max_length=100)
    collection_id = models.ForeignKey(
        AssetsCollection, on_delete=models.CASCADE, related_name='collection_id'
        )
    last_sale = models.CharField(max_length=100, blank=True)
    top_bid = models.CharField(max_length=100, blank=True)
    listing_date = models.CharField(max_length=100, blank=True)
    is_presale = models.CharField(max_length=100, blank=True)
    transfer_fee_payment_token = models.CharField(max_length=100, blank=True)
    transfer_fee = models.CharField(max_length=100, blank=True)
    sell_orders = models.CharField(max_length=100, blank=True)
    owner_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='owner'
        )
    creator_id = models.ForeignKey(
        AssetsUsers, on_delete=models.CASCADE, related_name='creator'
        )

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Asset'


