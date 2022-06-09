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


class NFTCollection(models.Model):
    collection_id               = models.CharField(max_length=255, blank=True)
    collection_url              = models.CharField(max_length=255, blank=True)
    slug                        = models.CharField(max_length=255, blank=True)
    collection_type             = models.CharField(max_length=255, blank=True)
    collection_name             = models.CharField(max_length=255, blank=True)
    collection_description      = models.TextField(blank=True, default='')
    trades	                    = models.CharField(max_length=255, blank=True)
    volume                      = models.CharField(max_length=255, blank=True)
    floor                       = models.CharField(max_length=255, blank=True)
    collection_symbol           = models.CharField(max_length=255, blank=True)
    owner                       = models.CharField(max_length=255, blank=True)
    external_image_url          = models.CharField(max_length=255, blank=True)
    aws_bucket_image_url        = models.CharField(max_length=255, blank=True)
    external_link               = models.CharField(max_length=255, blank=True)
    buyer_fee_basis_points      = models.CharField(max_length=255, blank=True)
    seller_fee_basis_points     = models.CharField(max_length=255, blank=True)
    twitter_username            = models.CharField(max_length=255, blank=True)
    discord_url                 = models.CharField(max_length=255, blank=True)
    updated_at                  = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NFT Collection'


# ========================================================================================================== #
# class AssetsUsers(models.Model):
#     user_type = models.CharField(max_length=254)
#     username = models.CharField(max_length=254, blank=True)
#     profile_img_url = models.CharField(max_length=254, blank=True)
#     address = models.CharField(max_length=254)
#     value = models.CharField(max_length=254, blank=True)

#     def __str__(self):
#         return self.username

#     class Meta:
#         verbose_name = 'Assets User'


# class AssetsImage(models.Model):
#     type = models.CharField(max_length=255, blank=True)
#     external_image_url = models.CharField(max_length=255)
#     aws_bucket_image_url = models.CharField(max_length=255)
#     representation = models.CharField(max_length=255)
#     mimeType = models.CharField(max_length=255)
#     size = models.CharField(max_length=255, blank=True)
#     width = models.CharField(max_length=255, blank=True)
#     height = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.url

#     class Meta:
#         verbose_name = 'Assets Image'


# class APIPaginate(models.Model):
#     total = models.CharField(max_length=255, blank=True)
#     continuation = models.CharField(max_length=255, blank=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.url

#     class Meta:
#         verbose_name = 'API Paginate'


# class BestOrders(models.Model):
#     order_id = models.CharField(max_length=255, blank=True)
#     makeprice = models.CharField(max_length=255, blank=True)
#     takeprice = models.CharField(max_length=255, blank=True)
#     maker = models.CharField(max_length=255, blank=True)
#     taker = models.CharField(max_length=255, blank=True)
#     type = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.order_id

#     class Meta:
#         verbose_name = 'Best Orders'


# class Assets(models.Model):
#     id = models.CharField(max_length=255, primary_key=True)
#     blockchain = models.CharField(max_length=255)
#     collection = models.CharField(max_length=255)
#     contract = models.CharField(max_length=255)
#     tokenId = models.CharField(max_length=255)
#     owner_id = models.ForeignKey(
#         AssetsUsers, on_delete=models.CASCADE, related_name='owner_id', blank=True, null=True
#     )
#     creator_id = models.ForeignKey(
#         AssetsUsers, on_delete=models.CASCADE, related_name='creator_id', blank=True, null=True
#     )
#     mintedAt = models.CharField(max_length=255)
#     lastUpdatedAt = models.CharField(max_length=255)
#     supply = models.CharField(max_length=255)
#     name = models.CharField(max_length=255, blank=True)
#     description = models.TextField(blank=True, default='')
#     image_id = models.ForeignKey(
#         AssetsImage, on_delete=models.CASCADE, related_name='image_id', blank=True, null=True
#     )
#     permalink = models.CharField(max_length=255, blank=True)
#     restriction = models.CharField(max_length=255, blank=True)
#     deleted = models.BooleanField(default=False)
#     auction = models.CharField(max_length=255, blank=True)
#     totalStock = models.CharField(max_length=255, blank=True)
#     sellers = models.IntegerField(default=0, blank=True)
#     status = models.CharField(max_length=255, blank=True)
#     platform = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Asset'

