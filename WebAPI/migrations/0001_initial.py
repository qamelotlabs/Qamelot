# Generated by Django 3.0.5 on 2022-05-31 11:53

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIPaginate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(blank=True, max_length=255)),
                ('continuation', models.CharField(blank=True, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'API Paginate',
            },
        ),
        migrations.CreateModel(
            name='AssetsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255)),
                ('external_image_url', models.CharField(max_length=255)),
                ('aws_bucket_image_url', models.CharField(max_length=255)),
                ('representation', models.CharField(max_length=255)),
                ('mimeType', models.CharField(max_length=255)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('width', models.CharField(blank=True, max_length=255)),
                ('height', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Assets Image',
            },
        ),
        migrations.CreateModel(
            name='AssetsUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=254)),
                ('username', models.CharField(blank=True, max_length=254)),
                ('profile_img_url', models.CharField(blank=True, max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('value', models.CharField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Assets User',
            },
        ),
        migrations.CreateModel(
            name='BestOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=255)),
                ('makeprice', models.CharField(blank=True, max_length=255)),
                ('takeprice', models.CharField(blank=True, max_length=255)),
                ('maker', models.CharField(blank=True, max_length=255)),
                ('taker', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Best Orders',
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
        migrations.CreateModel(
            name='TwwetData',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('author_id', models.CharField(blank=True, max_length=100)),
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
            name='AssetsCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_id', models.CharField(blank=True, max_length=255)),
                ('blockchain', models.CharField(blank=True, max_length=255)),
                ('colletion_type', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('symbol', models.CharField(blank=True, max_length=255)),
                ('owner', models.CharField(blank=True, max_length=255)),
                ('minters', models.CharField(blank=True, max_length=255)),
                ('external_link', models.CharField(blank=True, max_length=255)),
                ('fee_recipient', models.CharField(blank=True, max_length=255)),
                ('twitter_username', models.CharField(blank=True, max_length=255)),
                ('discord_url', models.CharField(blank=True, max_length=255)),
                ('seller_fee_basis_point', models.CharField(blank=True, max_length=255)),
                ('buyer_fee_basis_point', models.CharField(blank=True, max_length=255)),
                ('best_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best_order', to='WebAPI.BestOrders')),
                ('collection_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_image', to='WebAPI.AssetsImage')),
            ],
            options={
                'verbose_name': 'Assets Collection',
            },
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('blockchain', models.CharField(max_length=255)),
                ('collection', models.CharField(max_length=255)),
                ('contract', models.CharField(max_length=255)),
                ('tokenId', models.CharField(max_length=255)),
                ('mintedAt', models.CharField(max_length=255)),
                ('lastUpdatedAt', models.CharField(max_length=255)),
                ('supply', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('permalink', models.CharField(blank=True, max_length=255)),
                ('restriction', models.CharField(blank=True, max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('auction', models.CharField(blank=True, max_length=255)),
                ('totalStock', models.CharField(blank=True, max_length=255)),
                ('sellers', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('platform', models.CharField(blank=True, max_length=255)),
                ('asset_collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asset_collection', to='WebAPI.AssetsCollection')),
                ('creator_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_id', to='WebAPI.AssetsUsers')),
                ('image_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_id', to='WebAPI.AssetsImage')),
                ('owner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_id', to='WebAPI.AssetsUsers')),
            ],
            options={
                'verbose_name': 'Asset',
            },
        ),
    ]