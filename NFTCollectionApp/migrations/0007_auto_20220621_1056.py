# Generated by Django 3.0.5 on 2022-06-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NFTCollectionApp', '0006_auto_20220617_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nftcollection',
            name='averagePrice',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='count',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='floorPrice',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='marketCap',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='numOwners',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='numReports',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='oneDayAveragePrice',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='oneDayChange',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='oneDaySales',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='oneDayVolume',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='sevenDayAveragePrice',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='sevenDayChange',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='sevenDaySales',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='sevenDayVolume',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='thirtyDayAveragePrice',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='thirtyDayChange',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='thirtyDaySales',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='thirtyDayVolume',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='totalSales',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='totalSupply',
        ),
        migrations.RemoveField(
            model_name='nftcollection',
            name='totalVolume',
        ),
        migrations.CreateModel(
            name='collectionStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateLog', models.DateField(blank=True, null=True)),
                ('oneDayVolume', models.CharField(blank=True, max_length=255)),
                ('oneDayChange', models.CharField(blank=True, max_length=255)),
                ('oneDaySales', models.CharField(blank=True, max_length=255)),
                ('oneDayAveragePrice', models.CharField(blank=True, max_length=255)),
                ('sevenDayVolume', models.CharField(blank=True, max_length=255)),
                ('sevenDayChange', models.CharField(blank=True, max_length=255)),
                ('sevenDaySales', models.CharField(blank=True, max_length=255)),
                ('sevenDayAveragePrice', models.CharField(blank=True, max_length=255)),
                ('thirtyDayVolume', models.CharField(blank=True, max_length=255)),
                ('thirtyDayChange', models.CharField(blank=True, max_length=255)),
                ('thirtyDaySales', models.CharField(blank=True, max_length=255)),
                ('thirtyDayAveragePrice', models.CharField(blank=True, max_length=255)),
                ('totalVolume', models.CharField(blank=True, max_length=255)),
                ('totalSales', models.CharField(blank=True, max_length=255)),
                ('totalSupply', models.CharField(blank=True, max_length=255)),
                ('count', models.CharField(blank=True, max_length=255)),
                ('numOwners', models.CharField(blank=True, max_length=255)),
                ('averagePrice', models.CharField(blank=True, max_length=255)),
                ('numReports', models.CharField(blank=True, max_length=255)),
                ('marketCap', models.CharField(blank=True, max_length=255)),
                ('floorPrice', models.CharField(blank=True, max_length=255)),
                ('collectionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collectionId', to='NFTCollectionApp.NFTCollection')),
            ],
            options={
                'verbose_name': 'Collection Stat',
            },
        ),
    ]
