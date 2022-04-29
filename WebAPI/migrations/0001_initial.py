# Generated by Django 3.0 on 2022-04-29 10:10

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', imagekit.models.fields.ProcessedImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DigitialAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('blochain', models.CharField(max_length=100)),
                ('bid_price', models.CharField(max_length=100)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='WebAPI.Categories')),
                ('imageMedia', models.ManyToManyField(blank=True, to='WebAPI.PhotoMedia')),
            ],
        ),
    ]
