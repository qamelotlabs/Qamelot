from django.db import models
from TwitterApp.models import *


class UserDetail(models.Model):
    address             = models.CharField(max_length=555, blank=True)
    firstname           = models.CharField(max_length=255, blank=True)
    lastname            = models.CharField(max_length=255, blank=True)
    email               = models.CharField(max_length=255, blank=True)
    userImageUrl        = models.CharField(max_length=255, blank=True)
    influencers         = models.ManyToManyField(NftInfluencers, blank=True)
    createdAt           = models.DateField(blank=True, null=True)
    updatedAt           = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'User Detail'